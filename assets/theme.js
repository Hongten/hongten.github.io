(function () {
  const KEY = 'tomblog-theme';
  const root = document.documentElement;

  const moonIcon = `
    <svg viewBox="0 0 24 24" fill="none" aria-hidden="true">
      <path d="M21 13.2A9 9 0 1 1 10.8 3a7 7 0 1 0 10.2 10.2Z" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>`;

  const sunIcon = `
    <svg viewBox="0 0 24 24" fill="none" aria-hidden="true">
      <circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.8"/>
      <path d="M12 2v2.2M12 19.8V22M4.9 4.9l1.6 1.6M17.5 17.5l1.6 1.6M2 12h2.2M19.8 12H22M4.9 19.1l1.6-1.6M17.5 6.5l1.6-1.6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
    </svg>`;

  function getTheme() {
    return localStorage.getItem(KEY) || 'dark';
  }

  function setTheme(theme) {
    const value = theme === 'light' ? 'light' : 'dark';
    root.setAttribute('data-theme', value);
    localStorage.setItem(KEY, value);
  }

  function updateButton(btn, theme) {
    if (theme === 'dark') {
      btn.innerHTML = moonIcon;
      btn.title = 'Use Light';
      btn.setAttribute('aria-label', 'Use Light');
    } else {
      btn.innerHTML = sunIcon;
      btn.title = 'Use Dark';
      btn.setAttribute('aria-label', 'Use Dark');
    }
  }

  function mountControl() {
    const menu = document.querySelector('.menu');
    if (!menu || menu.querySelector('#appearanceBtn')) return;

    const btn = document.createElement('button');
    btn.id = 'appearanceBtn';
    btn.className = 'appearance-btn';
    btn.type = 'button';

    const apply = (theme) => {
      setTheme(theme);
      updateButton(btn, theme);
    };

    const cur = getTheme();
    apply(cur);

    btn.addEventListener('click', () => {
      const next = getTheme() === 'dark' ? 'light' : 'dark';
      apply(next);
    });

    menu.appendChild(btn); // place after GitHub menu
  }

  setTheme(getTheme()); // default dark

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mountControl);
  } else {
    mountControl();
  }
})();
