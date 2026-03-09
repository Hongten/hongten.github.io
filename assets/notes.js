(function () {
  const cfg = window.TOM_SUPABASE || {};
  const form = document.getElementById('noteForm');
  const formMsg = document.getElementById('formMsg');
  const searchInput = document.getElementById('noteSearch');
  const refreshBtn = document.getElementById('refreshBtn');
  const timelineEl = document.getElementById('timeline');
  const statsEl = document.getElementById('noteStats');

  const pageSizeSelect = document.getElementById('notePageSize');
  const prevPageBtn = document.getElementById('notePrevPage');
  const nextPageBtn = document.getElementById('noteNextPage');
  const pageInfoEl = document.getElementById('notePageInfo');

  const contentInput = document.getElementById('noteContent');

  let allNotes = [];
  let currentPage = 1;
  let pageSize = 10;

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

  function getFilteredNotes() {
    const q = (searchInput.value || '').trim().toLowerCase();
    if (!q) return allNotes;
    return allNotes.filter(n => (n.content || '').toLowerCase().includes(q));
  }

  function clampPage(page, totalPages) {
    return Math.min(Math.max(page, 1), Math.max(totalPages, 1));
  }

  function renderNotes() {
    const filtered = getFilteredNotes();
    const total = filtered.length;
    const totalPages = Math.max(1, Math.ceil(total / pageSize));
    currentPage = clampPage(currentPage, totalPages);

    const start = (currentPage - 1) * pageSize;
    const pageItems = filtered.slice(start, start + pageSize);

    if (!pageItems.length) {
      timelineEl.innerHTML = '<article class="card"><h2>暂无笔记</h2><p>先写一条，或者换个关键词搜索。</p></article>';
    } else {
      timelineEl.innerHTML = pageItems.map(n => {
        const content = n.content || '';
        const preview = content.length > 180 ? `${content.slice(0, 180)}...` : content;
        const hasMore = content.length > 180;
        return `
          <article class="card note-card">
            <div class="meta">记录时间：${fmtTime(n.created_at)}${n.updated_at ? ` · 更新时间：${fmtTime(n.updated_at)}` : ''}</div>
            <p class="note-content note-preview">${escapeHtml(preview).replaceAll('\n', '<br/>')}</p>
            ${hasMore ? `<details class="note-details"><summary>展开全文</summary><p class="note-content">${escapeHtml(content).replaceAll('\n', '<br/>')}</p></details>` : ''}
          </article>
        `;
      }).join('');
    }

    if (statsEl) statsEl.textContent = `共 ${total} 条记录`;
    if (pageInfoEl) pageInfoEl.textContent = `Page ${currentPage} / ${totalPages}`;
    if (prevPageBtn) prevPageBtn.disabled = currentPage <= 1;
    if (nextPageBtn) nextPageBtn.disabled = currentPage >= totalPages;
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
      const { error } = await client.from(table).insert({ content });
      if (error) throw error;

      form.reset();
      setMsg('已保存 ✅');
      currentPage = 1;
      await loadNotes();
    } catch (err) {
      setMsg(`保存失败：${err.message || String(err)}`, true);
    }
  }

  form.addEventListener('submit', createNote);
  searchInput.addEventListener('input', () => {
    currentPage = 1;
    renderNotes();
  });
  refreshBtn.addEventListener('click', loadNotes);

  if (pageSizeSelect) {
    pageSizeSelect.addEventListener('change', () => {
      pageSize = Number(pageSizeSelect.value) || 10;
      currentPage = 1;
      renderNotes();
    });
  }
  if (prevPageBtn) {
    prevPageBtn.addEventListener('click', () => {
      currentPage -= 1;
      renderNotes();
    });
  }
  if (nextPageBtn) {
    nextPageBtn.addEventListener('click', () => {
      currentPage += 1;
      renderNotes();
    });
  }

  loadNotes();
})();
