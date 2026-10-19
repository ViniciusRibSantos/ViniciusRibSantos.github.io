# Spec: Redesign "Internet dos anos 2000"

> Status: implementada · Autor: Vinicius Ribeiro · Data: 2026-10-19

## 1. Objetivo

Transformar o portfólio (`index.html`, `cv.html`, `projetos.html`) numa **home page pessoal do começo da internet (≈1997–2003)**, do tipo que se hospedava no GeoCities, HPG, Kit.net, Tripod ou Angelfire. A inspiração é a **própria web da época**: GIFs animados por todo lado, fundos com textura repetida, tabelas com bordas, `<marquee>`, contador de visitas, livro de visitas, webrings e selos "Melhor visualizado no Netscape". Não é uma imitação de sistema operacional: nada de janelas, botões chanfrados ou visual de Windows.

O resultado tem de parecer uma página feita à mão por alguém que acabou de aprender HTML, e não um tema "retrô" moderno. Mesmo assim, o conteúdo (experiência, formação, projetos e contatos) continua legível e fácil de achar por um recrutador.

### Não-objetivos

- Mudar o conteúdo do CV ou dos projetos (só o tom dos textos de interface muda).
- Adicionar backend, build step ou framework. O site continua estático no GitHub Pages.
- Reproduzir os incômodos reais da época: pop-ups de verdade, áudio que toca sozinho, scripts que travam a navegação.
- Imitar Windows/desktop (janelas, barra de título, botões cinza 3D).

## 2. Estado atual

| Item | Hoje |
|---|---|
| Páginas | `index.html` (hero), `cv.html` (timeline), `projetos.html` (grid de cards) |
| Estilo | `css/style.css` (433 linhas), tema escuro roxo, glassmorphism, fonte Inter |
| Dependências | Bootstrap 5.3 (CSS+JS), Font Awesome 5.7, Google Fonts |
| Navegação | navbar sticky com menu hambúrguer do Bootstrap |

Todas as dependências externas saem. Nenhuma delas existia em 2001, e sem elas o site carrega como "página de 56k".

## 3. Direção visual

### 3.1 Referências

- **Páginas pessoais do GeoCities/HPG:** fundo de estrelas ou textura repetida, título enorme em WordArt/GIF, `<marquee>`, contador, "em construção" e "assine meu livro de visitas".
- **GifCities** (gifcities.org, do Internet Archive): o acervo de GIFs do GeoCities. É a principal fonte de referência e de assets.
- **Cameron's World** (cameronsworld.net): colagem de fragmentos do GeoCities, boa referência de densidade e caos.
- **Space Jam (1996)** (spacejam.com/1996): o exemplo clássico de site da época ainda no ar.

### 3.2 Paleta

Cores "web-safe" e cores nomeadas do HTML, usadas sem medo:

| Token | Valor | Uso |
|---|---|---|
| `--bg` | `#000000` + GIF de estrelas em tile | fundo da página |
| `--content-bg` | `#FFFFCC` ou `#FFFFFF` | caixa central de leitura |
| `--text` | `#000000` | texto em áreas claras |
| `--text-on-dark` | `#FFFFFF` / `#FFFF00` | textos curtos sobre o fundo preto |
| `--link` / `--visited` / `--active` | `#0000FF` / `#800080` / `#FF0000` | links sublinhados clássicos |
| `--neon` | `#00FF00`, `#FF00FF`, `#00FFFF`, `#FFFF00` | títulos, `marquee`, selos "NOVO!" |
| `--borda-tabela` | `#FF00FF` ou `#00FFFF` | bordas das tabelas de conteúdo |

**Regra de legibilidade:** texto corrido (descrições do CV e dos projetos) fica sempre em preto sobre uma caixa clara. Cores neon sobre o preto só entram em títulos, banners e enfeites.

### 3.3 Tipografia

Sem webfonts, só a pilha do sistema, como na época:

- Corpo: `"Times New Roman", Times, serif`, 16px.
- Títulos chamativos: `"Comic Sans MS", "Comic Neue", cursive`, ou `Impact` / `Arial Black`, em cores neon e com `text-shadow` duro (sem blur).
- Título principal da home: um **GIF de texto animado** (fogo, brilho ou arco-íris) com o nome, no estilo dos geradores de logo da época, com o mesmo texto no `alt`.
- Menus e rodapé: `Verdana, Arial, sans-serif`, 12–13px.
- Datas: `"Courier New", monospace`.
- Textos em arco-íris (uma cor por letra) e `<font>`-style coloridos são permitidos nos enfeites.

### 3.4 GIFs: o elemento central

Os GIFs animados são o coração do visual. Cada página deve ter vários.

| GIF | Onde |
|---|---|
| Fundo de estrelas/galáxia em tile | todas as páginas |
| Título/logo animado (fogo, brilho, arco-íris) | topo da home |
| "Bem-vindo" girando ou piscando | home |
| Globo terrestre girando / computador / @ girando | home e menu |
| Placa "Em construção" e operário com picareta | projetos |
| Pombo-correio ("Fale comigo pelo LinkedIn!") | rodapé, ao lado do contato |
| "NOVO!" / "NEW!" piscando | itens de novidades |
| Divisórias animadas (linha de fogo, arco-íris, estrelinhas) | entre seções |
| Bolinhas/setas animadas como marcadores | menu e listas |
| Livro de visitas / caneta escrevendo | link do livro de visitas |
| Bandeira do Brasil tremulando | ao lado de "São Paulo, Brasil" no CV |
| Selos 88×31 ("Netscape Now!", "Feito com Bloco de Notas", "Get Internet Explorer", "Melhor em 800x600") | rodapé |

**Fonte e hospedagem dos GIFs:**

- Buscar no **GifCities** e salvar **localmente** em `img/gifs/`, sem hotlink.
- Quando faltar um GIF específico (por exemplo, o título com o nome), criar um próprio em pixel art no Aseprite, no mesmo estilo.
- Registrar a origem de cada GIF em `img/gifs/CREDITOS.md`.
- Cada GIF deve ter menos de 50 KB. Juntos, todos os GIFs de uma página somam no máximo 400 KB.

### 3.5 Outros elementos da web da época

| Elemento | Implementação |
|---|---|
| Faixa rolante | `<marquee>` real (os navegadores ainda suportam), com fallback ver §6 |
| Contador de visitas | dígitos em GIF estilo odômetro, valor fake persistido em `localStorage`, começando em `001337`; "Você é o visitante nº" |
| Livro de visitas | ver §5.4 |
| Webring | `[ << Anterior \| Aleatório \| Próximo >> ]` com o nome do anel ("Anel dos Devs Brasileiros") |
| Data de atualização | "Última atualização: 19/10/2001" (data fixa, de propósito) |
| "Adicione aos Favoritos!" | link decorativo que mostra um `alert()` com o atalho Ctrl+D |
| Rastro de estrelinhas no cursor | JS que gera brilhinhos atrás do mouse; desligado com movimento reduzido e em telas de toque |
| Tabelas com borda | `border` colorida, `cellpadding` aparente, células de cores diferentes |
| Texto centralizado | quase tudo centralizado, como se usasse `<center>` |
| `<hr>` | grosso, colorido ou trocado por GIF de divisória |

## 4. Layout

### 4.1 Estrutura geral

Página centralizada de **largura fixa de 760px** (cabe em 800×600), com cara de "tabela de layout" e menu lateral, muito comum na época:

```
              ★ ✦ fundo de estrelas em tile ✦ ★
┌──────────────────────────────────────────────┐
│   [GIF ANIMADO: "VINICIUS RIBEIRO" em fogo]  │
│   [globo girando]  Bem-vindo!  [globo]       │
├──────────────────────────────────────────────┤
│ <marquee> *** CV atualizado!!! *** ...       │
├────────────┬─────────────────────────────────┤
│ MENU       │                                 │
│ ● Início   │   caixa clara com o conteúdo    │
│ ● Currículo│   (borda colorida de 3px)       │
│ ● Projetos │                                 │
│ ● Livro de │   [GIF divisória de fogo]       │
│   Visitas  │                                 │
│ [@ girando]│                                 │
├────────────┴─────────────────────────────────┤
│ [GIF divisória arco-íris]                    │
│ Você é o visitante nº [0][0][1][3][3][7]     │
│ [envelope] Me mande um e-mail!               │
│ [88x31][88x31][88x31][88x31]                 │
│ << Anel dos Devs Brasileiros >>              │
│ Última atualização: 19/10/2001               │
└──────────────────────────────────────────────┘
```

- Coluna do menu: 160px, fundo de cor sólida (ex.: `#000066`), links com GIF de bolinha como marcador.
- O layout é feito com **CSS Grid/Flexbox** e as bordas de tabela vêm do CSS. Não usar `<table>` para layout, para manter a semântica e a acessibilidade; `<table>` real só para dado tabular, se houver.
- Item ativo do menu: seta animada `►` ao lado e texto em negrito amarelo.

### 4.2 Responsividade

Telas pequenas não existiam em 2001, mas o site precisa funcionar no celular:

- Abaixo de **780px**, a largura fixa vira `100%`, o menu lateral passa a uma faixa de links acima do conteúdo e os selos 88×31 quebram linha.
- Sem menu hambúrguer, porque também não existia. Os links cabem em uma ou duas linhas.
- GIFs grandes ganham `max-width: 100%`.
- Nada de rolagem horizontal da página inteira.

## 5. Páginas

### 5.1 `index.html`: "Home Page"

- Topo: GIF do nome animado, ladeado por globos girando, e embaixo **"Bem-vindo(a) à minha Home Page!!!"**.
- Caixa "Quem sou eu": parágrafo curto em primeira pessoa no tom da época ("Olá internauta! Eu sou o Vinicius, desenvolvedor de software de São Paulo..."), mantendo a informação real (cargo e área).
- Links grandes para "Meu Currículo" e "Meus Projetos", cada um com GIF (pasta, disquete, computador).
- Bloco "Novidades" com GIF "NOVO!" piscando e datas fictícias.
- Rodapé completo: contador, e-mail com envelope, selos e webring.

### 5.2 `cv.html`: "Meu Currículo"

- Título "Meu Currículo" em Comic Sans neon, com GIF de pergaminho ou diploma.
- Cabeçalho: nome, cargo, "São Paulo, Brasil" com bandeira tremulando e links para LinkedIn/GitHub como links azuis sublinhados.
- **Experiência** e **Formação** como `<h2>` coloridos, cada um com um GIF ao lado (maleta, capelo).
- Cada item numa caixa clara com borda colorida: cargo em negrito, empresa em itálico, período em `Courier New` e descrição.
- Divisória em GIF entre os itens.
- Link "Imprimir esta página" com GIF de impressora, que chama `window.print()` (funciona de verdade). Um `@media print` remove fundo e GIFs.
- Todo o texto atual do CV é mantido **sem alteração**.

### 5.3 `projetos.html`: "Meus Projetos"

- Título com GIF de computador ou disquete.
- Cada projeto numa linha da "tabela" com borda: GIF de pasta, nome como link, descrição.
- O mesmo projeto atual (Redes Neurais Artificiais em Python) com o mesmo link.
- GIF grande "Em construção" e o texto **"Mais projetos em breve!!! Volte sempre!"**, já que hoje há um único projeto.

### 5.4 `livro-de-visitas.html`: "Livro de Visitas" (recomendado)

Ícone do GeoCities e quase obrigatório no tema.

- Formulário visual (nome, cidade, "Como chegou aqui?", mensagem) que **não envia dados ao site**. O botão "Assinar!" abre uma issue no GitHub do repositório já preenchida com a assinatura. Escolhemos issue em vez de `mailto:` para não publicar o e-mail pessoal no site.
- Lista de "assinaturas" estática, com algumas mensagens de exemplo no tom da época, marcadas como exemplo.
- GIF de livro ou caneta no topo.

## 6. Animações e acessibilidade

O exagero visual não pode tornar o site inacessível:

- **Movimento:** com `prefers-reduced-motion: reduce`, a faixa rolante fica estática, nada pisca, o rastro do cursor é desligado e os GIFs animados são trocados pela versão estática (primeiro quadro) via `<picture>` com `media="(prefers-reduced-motion: reduce)"`. Para isso, cada GIF ganha um par `.png` estático.
- **Piscar:** o `blink` em CSS (`@keyframes` com `steps`) fica em no máximo **2 Hz** e só em selos pequenos ("NOVO!"), nunca em texto corrido, para respeitar a WCAG 2.3.1. Nenhum GIF pode piscar mais que 3 vezes por segundo em área grande.
- **Contraste:** todo texto de conteúdo tem contraste AA (≥ 4.5:1). Neon sobre preto passa fácil; neon sobre branco é proibido.
- **Semântica:** `<header>`, `<nav>`, `<main>` e `<footer>`, um `<h1>` por página (pode ser a imagem do título com `alt`), `lang="pt-br"`.
- **Imagens:** GIFs decorativos com `alt=""`; os informativos (título, selos, contador) com `alt` descritivo. O contador expõe o número como texto (`aria-label="Visitantes: 1337"`).
- **Foco:** os links mantêm um contorno de foco visível.
- **Sem áudio automático:** se houver um "player de MIDI" de brincadeira, ele começa pausado e só toca depois de um clique.

## 7. Implementação técnica

### 7.1 Arquivos

```
css/retro.css              # substitui css/style.css (que é removido)
js/retro.js                # contador, rastro do cursor, "Favoritos"; < 3 KB, sem dependências
img/gifs/                  # GIFs animados + versões .png estáticas + CREDITOS.md
img/selos/                 # selos 88x31
index.html, cv.html, projetos.html, livro-de-visitas.html
```

- Remover `<link>`/`<script>` de Bootstrap, Font Awesome e Google Fonts em todas as páginas.
- Trocar os ícones Font Awesome (LinkedIn, GitHub, calendário, mapa) por GIFs pequenos ou texto.
- Repetir o cabeçalho, o menu e o rodapé em cada HTML, como se fazia na época. É aceitável com quatro páginas; não criar um sistema de includes.
- O JS é **aprimoramento progressivo**: sem JS, o site funciona inteiro e o contador mostra um valor fixo.

### 7.2 Componentes CSS

| Classe | Descrição |
|---|---|
| `.pagina` | contêiner de 760px centralizado |
| `.caixa` | caixa clara de conteúdo com borda colorida grossa |
| `.titulo-neon` | título em Comic Sans/Impact com cor neon e sombra dura |
| `.arco-iris` | texto em degradê ou uma cor por letra |
| `.marquee` | faixa rolante (fallback CSS) |
| `.pisca` | animação de piscar, desativada com movimento reduzido |
| `.contador` | dígitos do odômetro |
| `.selo-88x31` | imagem de selo com `image-rendering: pixelated` |
| `.divisoria` | GIF de divisória centralizado |
| `.menu-lateral` | coluna de links com marcadores em GIF |

### 7.3 Orçamento de desempenho

- Peso total por página: **< 600 KB**, quase tudo em GIFs. Usar `loading="lazy"` nos GIFs abaixo da dobra.
- Nenhuma requisição para domínios externos.
- Lighthouse: Performance ≥ 90, Accessibility ≥ 95.

## 8. Tom dos textos de interface

Usar o "internetês" da época **só nos textos da interface**, nunca no conteúdo profissional:

- "Bem-vindo(a) à minha Home Page!!!", "Você é o visitante nº", "Assine meu livro de visitas!", "Adicione aos Favoritos!", "Esta página está em construção", "Volte sempre!", "Melhor visualizado em 800x600 com Netscape Navigator 4".
- Tudo em português do Brasil.

## 9. Critérios de aceite

1. Todas as páginas usam o novo layout (título animado ou neon, faixa rolante, menu lateral, caixa de conteúdo, rodapé com contador/selos/webring).
2. Cada página tem pelo menos 4 GIFs animados, todos hospedados localmente e listados em `CREDITOS.md`.
3. Todo o conteúdo atual (textos do CV, projeto, links do LinkedIn/GitHub) está presente e sem alterações de texto.
4. Não há requisição a CDN nem fonte externa (conferir na aba Network).
5. Com `prefers-reduced-motion: reduce` ativo, nada se move nem pisca e os GIFs aparecem estáticos.
6. Em 375px de largura não existe rolagem horizontal e o menu fica acessível sem JS.
7. Navegar só pelo teclado alcança todos os links, com foco visível.
8. Lighthouse Accessibility ≥ 95 e Performance ≥ 90 em todas as páginas.
9. O README é atualizado: tecnologias (HTML + CSS puros, sem Bootstrap) e a explicação do tema.

## 10. Plano de execução

1. Garimpar os GIFs no GifCities, salvar em `img/gifs/`, gerar as versões estáticas e preencher `CREDITOS.md`.
2. Criar no Aseprite os GIFs que faltarem (título com o nome, selos personalizados).
3. Escrever `css/retro.css` com tokens e componentes (§3 e §7.2).
4. Reescrever o `index.html` e validar o layout e a responsividade.
5. Migrar `cv.html` e `projetos.html` e criar `livro-de-visitas.html`.
6. Adicionar `js/retro.js` (contador, rastro do cursor, Favoritos).
7. Remover `css/style.css` e as dependências externas; atualizar o README.
8. Rodar os critérios de aceite (§9) e abrir o PR.

## 11. Decisões em aberto

Decididas na implementação:

- **Livro de visitas:** issue pré-preenchida no GitHub (sem publicar e-mail).
- **Fundo:** estrelas amarelas piscando sobre preto.
- **Rastro do cursor:** estrelinhas coloridas, só com mouse e sem movimento reduzido.
- **Easter egg do visitante 1.000.000:** ficou de fora.
