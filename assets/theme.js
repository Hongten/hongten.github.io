(function () {
  const KEY = 'tomblog-theme';
  const root = document.documentElement;

  function applyTheme(theme) {
    const value = theme === 'light' ? 'light' : 'dark';
    root.setAttribute('data-theme', value);
    localStorage.setItem(KEY, value);
  }

  function currentTheme() {
    return localStorage.getItem(KEY) || 'dark';
  }

  function mountControl() {
    const menu = document.querySelector('.menu');
    if (!menu || menu.querySelector('#appearanceSelect')) return;

    const select = document.createElement('select');
    select.id = 'appearanceSelect';
    select.className = 'appearance-select';
    select.innerHTML = '<option value="dark">Appearance: Dark</option><option value="light">Appearance: Light</option>';
    select.value = currentTheme();
    select.addEventListener('change', () => applyTheme(select.value));

    menu.insertBefore(select, menu.firstChild);
  }

  applyTheme(currentTheme());
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mountControl);
  } else {
    mountControl();
  }
})();
