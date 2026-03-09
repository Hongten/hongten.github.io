(function () {
  const cfg = window.TOM_SUPABASE || {};
  const form = document.getElementById('noteForm');
  const formMsg = document.getElementById('formMsg');
  const searchInput = document.getElementById('noteSearch');
  const refreshBtn = document.getElementById('refreshBtn');
  const timelineEl = document.getElementById('timeline');

  const contentInput = document.getElementById('noteContent');

  let allNotes = [];

  function fmtTime(v) {
    const d = new Date(v);
    if (Number.isNaN(d.getTime())) return v || '-';
    return d.toLocaleString('zh-CN', { hour12: false });
  }

  function escapeHtml(s) {
    return String(s || '')
      .replaceAll('&', '&amp;')
      .replaceAll('<', '&lt;')
      .replaceAll('>', '&gt;')
      .replaceAll('"', '&quot;')
      .replaceAll("'", '&#39;');
  }

  function setMsg(text, isError) {
    formMsg.textContent = text || '';
    formMsg.style.color = isError ? '#f87171' : '';
  }

  function ensureClient() {
    if (!cfg.url || !cfg.anonKey) {
      throw new Error('请先在 assets/supabase-config.js 中填写 Supabase URL 和 anonKey。');
    }
    if (!window.supabase || !window.supabase.createClient) {
      throw new Error('Supabase SDK 加载失败。');
    }
    return window.supabase.createClient(cfg.url, cfg.anonKey);
  }

  function groupByMonth(notes) {
    const map = new Map();
    notes.forEach(n => {
      const d = new Date(n.created_at);
      const key = Number.isNaN(d.getTime())
        ? '未知时间'
        : `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}`;
      if (!map.has(key)) map.set(key, []);
      map.get(key).push(n);
    });
    return [...map.entries()].sort((a, b) => b[0].localeCompare(a[0]));
  }

  function renderNotes() {
    const q = (searchInput.value || '').trim().toLowerCase();
    const filtered = !q
      ? allNotes
      : allNotes.filter(n => (n.content || '').toLowerCase().includes(q));

    if (!filtered.length) {
      timelineEl.innerHTML = '<article class="card"><h2>暂无笔记</h2><p>先写一条，或者换个关键词搜索。</p></article>';
      return;
    }

    const groups = groupByMonth(filtered);
    timelineEl.innerHTML = groups.map(([month, items]) => `
      <section class="timeline-group">
        <h2 class="timeline-title">${month}</h2>
        ${items.map(n => `
          <article class="card note-card">
            <div class="meta">记录时间：${fmtTime(n.created_at)}${n.updated_at ? ` · 更新时间：${fmtTime(n.updated_at)}` : ''}</div>
            <p class="note-content">${escapeHtml(n.content || '').replaceAll('\n', '<br/>')}</p>
          </article>
        `).join('')}
      </section>
    `).join('');
  }

  async function loadNotes() {
    try {
      const client = ensureClient();
      const table = cfg.table || 'reading_notes';
      const { data, error } = await client
        .from(table)
        .select('id,content,created_at,updated_at')
        .order('created_at', { ascending: false });
      if (error) throw error;
      allNotes = data || [];
      renderNotes();
    } catch (err) {
      timelineEl.innerHTML = `<article class="card"><h2>加载失败</h2><p>${escapeHtml(err.message || String(err))}</p></article>`;
    }
  }

  async function createNote(evt) {
    evt.preventDefault();
    setMsg('保存中...');

    const content = contentInput.value.trim();

    if (!content) {
      setMsg('内容不能为空。', true);
      return;
    }

    try {
      const client = ensureClient();
      const table = cfg.table || 'reading_notes';
      const payload = { content };
      const { error } = await client.from(table).insert(payload);
      if (error) throw error;

      form.reset();
      setMsg('已保存 ✅');
      await loadNotes();
    } catch (err) {
      setMsg(`保存失败：${err.message || String(err)}`, true);
    }
  }

  form.addEventListener('submit', createNote);
  searchInput.addEventListener('input', renderNotes);
  refreshBtn.addEventListener('click', loadNotes);

  loadNotes();
})();
