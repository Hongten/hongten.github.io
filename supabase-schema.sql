-- Supabase schema for reading notes (anonymous write with rate-limit protection)
create extension if not exists pgcrypto;

create table if not exists public.reading_notes (
  id uuid primary key default gen_random_uuid(),
  content text not null,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

-- Compatible migration from old structure
alter table public.reading_notes alter column content set not null;
alter table public.reading_notes drop column if exists title;
alter table public.reading_notes drop column if exists tags;
alter table public.reading_notes drop column if exists user_id;

create or replace function public.set_updated_at()
returns trigger as $$
begin
  new.updated_at = now();
  return new;
end;
$$ language plpgsql;

drop trigger if exists trg_reading_notes_updated_at on public.reading_notes;
create trigger trg_reading_notes_updated_at
before update on public.reading_notes
for each row execute function public.set_updated_at();

alter table public.reading_notes enable row level security;

-- clean old policies
 drop policy if exists "notes_select_all" on public.reading_notes;
 drop policy if exists "notes_insert_all" on public.reading_notes;
 drop policy if exists "notes_insert_authenticated" on public.reading_notes;
 drop policy if exists "notes_update_owner" on public.reading_notes;
 drop policy if exists "notes_delete_owner" on public.reading_notes;
 drop policy if exists "notes_insert_rate_limited" on public.reading_notes;

-- public read
create policy "notes_select_all" on public.reading_notes
for select
using (true);

-- anonymous/public insert with global rate limit
-- allows up to 6 inserts per minute across whole table
create policy "notes_insert_rate_limited" on public.reading_notes
for insert
with check (
  length(trim(content)) between 1 and 5000
  and (
    select count(*)
    from public.reading_notes
    where created_at > now() - interval '1 minute'
  ) < 6
);
