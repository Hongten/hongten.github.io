-- Supabase schema for reading notes (free-tier friendly)
create extension if not exists pgcrypto;

create table if not exists public.reading_notes (
  id uuid primary key default gen_random_uuid(),
  title text not null,
  content text not null,
  tags text[] not null default '{}',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

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

-- Demo policy: anonymous read/write enabled (quick start for personal site).
-- If you later add auth, tighten these policies.
drop policy if exists "notes_select_all" on public.reading_notes;
create policy "notes_select_all" on public.reading_notes
for select
using (true);

drop policy if exists "notes_insert_all" on public.reading_notes;
create policy "notes_insert_all" on public.reading_notes
for insert
with check (true);
