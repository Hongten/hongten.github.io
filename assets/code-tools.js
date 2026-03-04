(function () {
  function fallbackCopy(text) {
    const ta = document.createElement('textarea');
    ta.value = text;
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
  }

  async function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(text);
    } else {
      fallbackCopy(text);
    }
  }

  function bindCopy(button, codeEl, label = 'Copy') {
    button.addEventListener('click', async () => {
      try {
        await copyText(codeEl.innerText);
        const old = button.textContent;
        button.textContent = 'Copied';
        setTimeout(() => (button.textContent = old), 1200);
      } catch {
        button.textContent = 'Failed';
        setTimeout(() => (button.textContent = label), 1200);
      }
    });
  }

  // Plain pre>code blocks (legacy)
  document.querySelectorAll('pre > code').forEach((code) => {
    if (code.closest('.tab-pane')) return;
    const pre = code.parentElement;
    const wrapper = document.createElement('div');
    wrapper.className = 'code-block';
    pre.parentNode.insertBefore(wrapper, pre);
    wrapper.appendChild(pre);

    const btn = document.createElement('button');
    btn.className = 'copy-btn';
    btn.type = 'button';
    btn.textContent = 'Copy';
    bindCopy(btn, code, 'Copy');
    wrapper.appendChild(btn);
  });

  // Tabbed code blocks
  document.querySelectorAll('.code-tabs').forEach((tabs) => {
    const tabBtns = tabs.querySelectorAll('.tab-btn');
    const panes = tabs.querySelectorAll('.tab-pane');

    function activate(lang) {
      tabBtns.forEach((btn) => btn.classList.toggle('active', btn.dataset.tab === lang));
      panes.forEach((pane) => {
        const isActive = pane.dataset.tab === lang;
        pane.classList.toggle('active', isActive);
        const copyBtn = pane.querySelector('.copy-btn');
        if (copyBtn && isActive) {
          const label = `Copy ${lang.charAt(0).toUpperCase()}${lang.slice(1)}`;
          copyBtn.textContent = label;
          copyBtn.dataset.defaultLabel = label;
        }
      });
    }

    tabBtns.forEach((btn) => {
      btn.addEventListener('click', () => activate(btn.dataset.tab));
    });

    panes.forEach((pane) => {
      const code = pane.querySelector('code');
      if (!code) return;
      if (!pane.querySelector('.copy-btn')) {
        const btn = document.createElement('button');
        btn.className = 'copy-btn';
        btn.type = 'button';
        const lang = pane.dataset.tab || 'code';
        const label = `Copy ${lang.charAt(0).toUpperCase()}${lang.slice(1)}`;
        btn.textContent = label;
        bindCopy(btn, code, label);
        pane.appendChild(btn);
      }
    });

    const first = tabBtns[0]?.dataset.tab;
    if (first) activate(first);
  });
})();
