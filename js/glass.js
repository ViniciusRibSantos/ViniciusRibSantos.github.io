(function () {
  var raiz = document.documentElement;
  var semMovimento = matchMedia('(prefers-reduced-motion: reduce)');

  // Refração: só o Chromium renderiza backdrop-filter com url().
  var marcas = (navigator.userAgentData && navigator.userAgentData.brands) || [];
  var chromium = marcas.some(function (m) { return m.brand === 'Chromium'; });
  if (chromium && CSS.supports('backdrop-filter', 'url(#liquid)')) {
    raiz.classList.add('refracao');
  }

  // A tab bar encolhe ao rolar para baixo e volta ao rolar para cima.
  var tabbar = document.querySelector('.tabbar');
  var ultimoY = window.scrollY;
  var agendado = false;

  window.addEventListener('scroll', function () {
    if (agendado) return;
    agendado = true;
    requestAnimationFrame(function () {
      var y = window.scrollY;
      if (semMovimento.matches || y < 80) {
        tabbar.classList.remove('tabbar--compacta');
      } else if (y > ultimoY + 4) {
        tabbar.classList.add('tabbar--compacta');
      } else if (y < ultimoY - 4) {
        tabbar.classList.remove('tabbar--compacta');
      }
      ultimoY = y;
      agendado = false;
    });
  }, { passive: true });

  // Brilho que segue o ponteiro.
  if (matchMedia('(pointer: fine)').matches) {
    document.addEventListener('pointermove', function (e) {
      if (semMovimento.matches) return;
      var alvo = e.target.closest && e.target.closest('.glass, .cartao');
      if (!alvo) return;
      var r = alvo.getBoundingClientRect();
      alvo.style.setProperty('--mx', (e.clientX - r.left) + 'px');
      alvo.style.setProperty('--my', (e.clientY - r.top) + 'px');
    }, { passive: true });
  }
})();
