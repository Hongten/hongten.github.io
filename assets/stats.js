(function () {
  const NS = 'openclaw-tomblog';
  const BASE = 'https://api.countapi.xyz';

  function normalizePath(pathname) {
    if (!pathname || pathname === '/') return 'home';
    return pathname.replace(/^\/+|\/+$/g, '').replace(/[^a-zA-Z0-9/_-]/g, '_') || 'home';
  }

  async function hit(key) {
    const res = await fetch(`${BASE}/hit/${NS}/${encodeURIComponent(key)}`);
    return res.json();
  }

  async function get(key) {
    const res = await fetch(`${BASE}/get/${NS}/${encodeURIComponent(key)}`);
    return res.json();
  }

  function setText(id, value) {
    const el = document.getElementById(id);
    if (el) el.textContent = value;
  }

  async function run() {
    const pageKey = `page:${normalizePath(location.pathname)}`;
    const totalKey = 'site:total';

    const pageSessionKey = `visited:${pageKey}`;
    const totalSessionKey = 'visited:site-total';

    try {
      const pageData = sessionStorage.getItem(pageSessionKey)
        ? await get(pageKey)
        : await hit(pageKey);
      if (!sessionStorage.getItem(pageSessionKey)) sessionStorage.setItem(pageSessionKey, '1');
      setText('pageVisits', (pageData.value ?? 0).toLocaleString());
    } catch {
      setText('pageVisits', 'N/A');
    }

    try {
      const totalData = sessionStorage.getItem(totalSessionKey)
        ? await get(totalKey)
        : await hit(totalKey);
      if (!sessionStorage.getItem(totalSessionKey)) sessionStorage.setItem(totalSessionKey, '1');
      setText('totalVisits', (totalData.value ?? 0).toLocaleString());
    } catch {
      setText('totalVisits', 'N/A');
    }
  }

  run();
})();
