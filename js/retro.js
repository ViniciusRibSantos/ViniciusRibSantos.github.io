// Scripts da Home Page do Vinicius. Tudo aqui é enfeite: sem JS a página funciona igual.
(function () {
  var reduzirMovimento = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Contador de visitas (de mentirinha, guardado no navegador do visitante)
  var contador = document.querySelector("[data-contador]");
  if (contador) {
    var visitas = 1337;
    try {
      visitas = (parseInt(localStorage.getItem("visitas"), 10) || 1336) + 1;
      localStorage.setItem("visitas", visitas);
    } catch (e) {}
    var digitos = String(visitas).padStart(6, "0");
    contador.innerHTML = digitos.split("").map(function (d) {
      return "<span>" + d + "</span>";
    }).join("");
    contador.setAttribute("aria-label", "Visitantes: " + visitas);
  }

  // "Adicione aos Favoritos!"
  document.querySelectorAll(".favoritos").forEach(function (link) {
    link.addEventListener("click", function (e) {
      e.preventDefault();
      var tecla = /Mac/.test(navigator.platform) ? "Cmd+D" : "Ctrl+D";
      alert("Aperte " + tecla + " para adicionar esta página aos seus Favoritos!");
    });
  });

  // Livro de visitas: abre uma issue no GitHub com a assinatura preenchida
  var form = document.querySelector("[data-livro-de-visitas]");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var d = new FormData(form);
      var corpo = "**Nome:** " + d.get("nome") +
        "\n**Cidade:** " + (d.get("cidade") || "-") +
        "\n**Como chegou aqui:** " + d.get("origem") +
        "\n\n" + d.get("mensagem");
      var url = form.action +
        "?title=" + encodeURIComponent("Livro de Visitas: " + d.get("nome")) +
        "&body=" + encodeURIComponent(corpo);
      window.open(url, "_blank", "noopener");
    });
  }

  // Rastro de estrelinhas atrás do mouse
  if (!reduzirMovimento && window.matchMedia("(pointer: fine)").matches) {
    var ultimo = 0;
    var cores = ["#FFFF00", "#FF00FF", "#00FFFF", "#00FF00"];
    document.addEventListener("mousemove", function (e) {
      var agora = Date.now();
      if (agora - ultimo < 50) return;
      ultimo = agora;
      var brilho = document.createElement("span");
      brilho.className = "brilho";
      brilho.setAttribute("aria-hidden", "true");
      brilho.textContent = "*";
      brilho.style.left = e.clientX + 6 + "px";
      brilho.style.top = e.clientY + 6 + "px";
      brilho.style.color = cores[Math.floor(Math.random() * cores.length)];
      document.body.appendChild(brilho);
      setTimeout(function () { brilho.remove(); }, 700);
    });
  }
})();
