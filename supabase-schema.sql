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

-- 登录保护版本：读取公开，写入仅登录用户。
alter table public.reading_notes add column if not exists user_id uuid references auth.users(id);
alter table public.reading_notes alter column user_id set default auth.uid();

-- 兼容旧策略
 drop policy if exists "notes_select_all" on public.reading_notes;
 drop policy if exists "notes_insert_all" on public.reading_notes;

create policy "notes_select_all" on public.reading_notes
for select
using (true);

create policy "notes_insert_authenticated" on public.reading_notes
for insert
to authenticated
with check (auth.uid() = user_id);

create policy "notes_update_owner" on public.reading_notes
for update
to authenticated
using (auth.uid() = user_id)
with check (auth.uid() = user_id);

create policy "notes_delete_owner" on public.reading_notes
for delete
to authenticated
using (auth.uid() = user_id);
