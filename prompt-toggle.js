/* Simple / Detailed prompt toggle + copy-the-visible-variant.
   Progressive enhancement: with JS off, the simple prompt stays visible. */
(function () {
  function visiblePre(box) {
    return box.querySelector('pre:not([hidden])') || box.querySelector('pre');
  }

  document.addEventListener('click', function (e) {
    var modeBtn = e.target.closest('.pmode button');
    if (modeBtn) {
      var box = modeBtn.closest('.prompt');
      var want = modeBtn.getAttribute('data-v');
      box.querySelectorAll('.pmode button').forEach(function (b) {
        var on = b === modeBtn;
        b.classList.toggle('on', on);
        b.setAttribute('aria-pressed', on ? 'true' : 'false');
      });
      box.querySelectorAll('pre[data-v]').forEach(function (p) {
        p.hidden = p.getAttribute('data-v') !== want;
      });
      return;
    }

    var copyBtn = e.target.closest('.prompt .copy');
    if (copyBtn) {
      var pre = visiblePre(copyBtn.closest('.prompt'));
      if (!pre || !navigator.clipboard) return;
      navigator.clipboard.writeText(pre.innerText);
      copyBtn.textContent = 'Copied';
      setTimeout(function () { copyBtn.textContent = 'Copy'; }, 1400);
    }
  });
})();
