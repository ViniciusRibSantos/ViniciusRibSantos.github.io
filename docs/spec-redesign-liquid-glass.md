# Spec: Redesign "Liquid Glass"

> Status: implementada · Autor: Vinicius Ribeiro · Data: 2026-10-21 · Base: `master`

## 1. Objetivo

Redesenhar o portfólio (`index.html`, `cv.html`, `projetos.html`) com a linguagem visual **Liquid Glass**, que a Apple apresentou na WWDC 2025 para o iOS 26, o macOS Tahoe e os demais sistemas. A ideia central é que os controles e as superfícies de navegação são feitos de um **vidro líquido**: translúcido, que refrata o que está atrás, tem brilho especular nas bordas e reage ao conteúdo e à interação.

O site deve parecer um app nativo da Apple rodando no navegador: navegação flutuante em cápsula, cartões de vidro sobre um fundo vivo, cantos concêntricos e movimento fluido. O conteúdo (experiência, formação, projetos e contatos) continua sendo o protagonista: o vidro é uma camada de navegação e de agrupamento, não decoração sobre o texto.

### Não-objetivos

- Mudar o conteúdo do CV ou dos projetos.
- Adicionar backend, build step ou framework. O site continua estático no GitHub Pages.
- Copiar assets proprietários da Apple (ícones SF Symbols, wallpapers, fontes SF Pro hospedadas por nós).
- Garantir efeito idêntico em todos os navegadores: a refração completa é um aprimoramento progressivo (ver §5.2).

## 2. Estado atual (`master`)

| Item | Hoje |
|---|---|
| Páginas | `index.html` (hero), `cv.html` (timeline), `projetos.html` (grid de cards) |
| Estilo | `css/style.css` (433 linhas), tema escuro roxo, `backdrop-filter` só na navbar, fonte Inter |
| Dependências | Bootstrap 5.3 (CSS+JS), Font Awesome 5.7, Google Fonts (Inter) |
| Navegação | navbar sticky com menu hambúrguer do Bootstrap |

O tema atual já flerta com glassmorphism, mas é "vidro fosco" estático: blur uniforme, sem refração, sem brilho e sem resposta à interação. O redesign troca isso por um material de verdade e remove as dependências externas.

## 3. Princípios do Liquid Glass

Resumo do que a Apple descreve nas Human Interface Guidelines e nas sessões da WWDC 2025 ("Meet Liquid Glass", "Get to know the new design system"), traduzido para o site:

1. **Hierarquia:** o vidro fica na camada de **navegação e controles**, flutuando acima do conteúdo. O conteúdo em si (texto do CV) fica em superfícies mais sólidas e legíveis.
2. **Lente, não blur:** o material dobra e concentra a luz do que está atrás (refração nas bordas), em vez de só desfocar.
3. **Brilho especular:** uma borda de luz fina acompanha o formato e reage ao movimento (do ponteiro, no nosso caso).
4. **Adaptatividade:** a tonalidade do vidro e do texto se ajusta ao que está por baixo (claro/escuro) para manter o contraste.
5. **Fluidez:** os elementos se transformam em vez de aparecer e sumir (a cápsula da navegação encolhe ao rolar; o indicador da aba ativa desliza como uma gota).
6. **Concentricidade:** cantos arredondados que se aninham (raio interno = raio externo − padding) e formas de cápsula.
7. **Nada de vidro sobre vidro:** não empilhar duas camadas de vidro; agrupar controles numa só superfície.

## 4. Direção visual

### 4.1 Referências

- Apple Human Interface Guidelines, seção *Materials* e página *Liquid Glass*.
- Sessões da WWDC 2025: "Meet Liquid Glass" e "Get to know the new design system".
- Tab bar e barra de busca do Safari e do app Música no iOS 26 (cápsula flutuante que encolhe ao rolar).
- Widgets e Dock do macOS Tahoe (vidro sobre wallpaper colorido).
- Experimentos web de "liquid glass" com `feDisplacementMap` em SVG (referência técnica para §5.2).

### 4.2 Fundo ("wallpaper")

O vidro só aparece se houver algo vivo atrás. Todas as páginas usam um fundo fixo (`position: fixed`) feito em CSS, sem imagens pesadas:

- 3 ou 4 "blobs" de cor grandes, com `radial-gradient` e `filter: blur()`, em azul, violeta, rosa e laranja (inspirados nos wallpapers padrão do iOS 26).
- Os blobs se movem devagar (ciclo de 30–60 s) e param com movimento reduzido.
- Uma camada sutil de ruído (SVG `feTurbulence` inline, opacidade ≤ 4%) evita banding nos gradientes.
- Variante clara e escura do wallpaper, seguindo `prefers-color-scheme`.

### 4.3 Paleta e tokens

| Token | Claro | Escuro | Uso |
|---|---|---|---|
| `--bg` | `#F2F2F7` | `#000000` | base sob o wallpaper |
| `--blob-1..4` | `#0A84FF`, `#BF5AF2`, `#FF375F`, `#FF9F0A` | os mesmos, com saturação menor | wallpaper |
| `--glass-tint` | `rgb(255 255 255 / 0.18)` | `rgb(30 30 32 / 0.28)` | preenchimento do vidro |
| `--glass-stroke` | `rgb(255 255 255 / 0.55)` | `rgb(255 255 255 / 0.22)` | borda especular |
| `--glass-shadow` | `0 8px 32px rgb(0 0 0 / 0.12)` | `0 8px 32px rgb(0 0 0 / 0.45)` | sombra de elevação |
| `--surface` | `rgb(255 255 255 / 0.72)` | `rgb(28 28 30 / 0.72)` | cartões de conteúdo (mais opacos) |
| `--label` | `#000000` | `#FFFFFF` | texto primário |
| `--label-2` | `rgb(60 60 67 / 0.75)` | `rgb(235 235 245 / 0.7)` | texto secundário |
| `--tint` | `#007AFF` | `#0A84FF` | links e ação primária (azul do sistema) |

As cores seguem as cores de sistema da Apple. O tema escuro passa a seguir o sistema do visitante, não fica mais fixo.

### 4.4 Tipografia

- Pilha do sistema, sem webfont: `-apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`. No Apple, isso já é a SF Pro; nos outros, uma fonte equivalente do sistema.
- Títulos grandes no estilo "Large Title": 34px (mobile) até 56px (desktop) com `clamp()`, peso 700, `letter-spacing: -0.02em`.
- Corpo: 17px, `line-height: 1.47` (o "Body" do iOS).
- Secundário/legendas: 13–15px em `--label-2`.
- Datas e períodos: `font-variant-numeric: tabular-nums`.

### 4.5 Forma e espaçamento

- Grade de 8px.
- Raios: cápsula (`border-radius: 999px`) para navegação e botões; 28px para cartões grandes; 20px para cartões internos. Elementos aninhados respeitam a concentricidade (`raio interno = raio externo − padding`).
- Ícones: SVG inline com traço de 1.5–2px, no estilo dos SF Symbols, desenhados por nós (LinkedIn e GitHub usam os logos oficiais das marcas em SVG).

## 5. O material de vidro

### 5.1 Camadas do componente `.glass`

Cada superfície de vidro é montada com:

1. **Backdrop:** `backdrop-filter: blur(12px) saturate(180%)` (com prefixo `-webkit-` para o Safari).
2. **Tint:** `background: var(--glass-tint)`.
3. **Borda especular:** `box-shadow: inset 0 1px 0 var(--glass-stroke), inset 0 0 0 1px rgb(255 255 255 / 0.08)`, mais um pseudo-elemento `::before` com `linear-gradient` em ângulo e `mask` só na borda, para o brilho que contorna a forma.
4. **Sombra de elevação:** `var(--glass-shadow)`.
5. **Brilho que segue o ponteiro (opcional):** um `radial-gradient` em `::after` posicionado por variáveis `--mx`/`--my` atualizadas por JS no `pointermove`.

### 5.2 Refração (aprimoramento progressivo)

A distorção de lente é o que separa o Liquid Glass do glassmorphism comum. Na web, ela é feita com um filtro SVG (`feTurbulence`/imagem de mapa + `feDisplacementMap`) aplicado via `backdrop-filter: url(#liquid)`.

- Hoje isso só funciona em navegadores Chromium. No Safari e no Firefox, o site usa só a pilha da §5.1 (que já fica muito boa).
- Detecção com `@supports (backdrop-filter: url(#x))` mais uma checagem em JS (`CSS.supports`), aplicando a classe `.glass--refract` só onde funciona.
- A refração fica concentrada nas bordas (mapa de deslocamento radial), com o centro quase sem distorção para não atrapalhar a leitura.
- Usar refração **só na navegação e nos botões**, nunca nos cartões com texto longo.

### 5.3 Variantes

| Variante | Uso | Características |
|---|---|---|
| `.glass` (regular) | navegação, botões, chips | tint leve, refração, brilho |
| `.glass--clear` | botão de ação sobre o hero | quase sem tint, mais transparente |
| `.surface` | cartões do CV e dos projetos | mais opaco (`--surface`), blur maior, sem refração, para leitura |

## 6. Layout por página

### 6.1 Navegação (todas as páginas)

- **Tab bar flutuante em cápsula**, centralizada no topo (desktop) ou no rodapé da tela (mobile ≤ 600px, como no iOS 26), com 16px de distância da borda.
- Itens: Início (ícone de casa), CV e Projetos. O item ativo tem um **indicador em forma de gota** que desliza entre os itens ao navegar (View Transitions API onde houver suporte; sem ela, troca simples).
- Ao rolar para baixo, a cápsula **encolhe** (escala menor no desktop, só ícones no mobile) e volta ao rolar para cima. Feito com um listener de `scroll` leve em JS (um `requestAnimationFrame` por quadro); sem JS, a cápsula fica sempre no tamanho normal.
- Sem menu hambúrguer: três itens cabem em qualquer largura.

### 6.2 `index.html`

- Hero centralizado sobre o wallpaper: "Olá, sou", nome em Large Title e "Desenvolvedor de Software".
- Os dois botões ("Ver Projetos" e "Ver CV") viram **cápsulas de vidro** lado a lado; "Ver Projetos" usa o `--tint` como cor de preenchimento (botão proeminente), "Ver CV" usa `.glass`.
- Ao pressionar, o botão "afunda" e se expande levemente (`scale(0.97)` → `scale(1.02)` com mola), simulando o comportamento elástico do Liquid Glass.
- Rodapé: chips de vidro com os ícones do LinkedIn e do GitHub.

### 6.3 `cv.html`

- Cabeçalho num cartão `.surface` grande (raio 28px): nome, cargo, local e dois chips de link (LinkedIn, GitHub).
- Seções "Experiência" e "Formação Acadêmica" com títulos no estilo de cabeçalho de lista agrupada do iOS (13px, caixa alta, `--label-2`).
- Cada experiência é uma linha de uma **lista agrupada** (estilo Ajustes do iOS): cargo em negrito, empresa em `--tint`, período e local em secundário e a descrição abaixo. As linhas ficam separadas por divisórias finas dentro do mesmo cartão, em vez de um cartão por item (o que evita vidro sobre vidro).
- Cabeçalho da seção fica sticky com um vidro fino ao rolar, como os títulos de seção do iOS.

### 6.4 `projetos.html`

- Título em Large Title e o subtítulo "Uma seleção dos meus repositórios e trabalhos."
- Grade de cartões `.surface` (mínimo 280px por coluna). Cada cartão tem nome, descrição e um botão-cápsula "Ver no GitHub" com ícone de seta para fora.
- Hover/foco: o cartão sobe 4px, a sombra aumenta e o brilho da borda acompanha o ponteiro.

## 7. Movimento

- Curvas: mola (`cubic-bezier(0.34, 1.56, 0.64, 1)`) para interações de toque e `ease-out` de 250–400 ms para entradas.
- Entrada da página: os cartões aparecem com fade + `translateY(8px)` em cascata (50 ms entre eles).
- Navegação entre páginas: View Transitions API (`@view-transition { navigation: auto; }`) com a cápsula da navegação marcada como `view-transition-name` para ela "ficar" enquanto o conteúdo troca.
- Wallpaper animado devagar (§4.2).
- Tudo isso desliga com `prefers-reduced-motion: reduce`.

## 8. Acessibilidade

O Liquid Glass recebeu críticas de legibilidade no lançamento, então esta seção é obrigatória:

- **Contraste:** todo texto tem contraste AA (≥ 4.5:1; ≥ 3:1 para texto grande) medido sobre o **pior caso** do wallpaper por trás. Por isso o texto longo fica sempre em `.surface`, nunca em vidro claro.
- **`prefers-reduced-transparency: reduce`:** o vidro vira superfície sólida (`--surface` com opacidade 0.96, sem blur nem refração). O mesmo vale para `prefers-contrast: more`, que ainda ganha borda de 1px sólida.
- **`prefers-reduced-motion: reduce`:** sem wallpaper animado, sem mola, sem cascata, sem encolher a navegação e sem brilho que segue o ponteiro.
- **Foco:** anel de foco visível (`outline: 2px solid var(--tint); outline-offset: 2px`) em links e botões, que acompanha o raio do elemento.
- **Semântica:** `<header>`, `<nav aria-label="Principal">`, `<main>` e `<footer>`; um `<h1>` por página; `aria-current="page"` no item ativo da navegação; `lang="pt-br"`.
- **Ícones:** decorativos com `aria-hidden="true"`; links só com ícone (casa, LinkedIn, GitHub) têm `aria-label`.
- **Alvo de toque:** no mínimo 44×44px, como pedem as HIG.

## 9. Implementação técnica

### 9.1 Arquivos

```
css/glass.css      # substitui css/style.css (que é removido): tokens, wallpaper, .glass, .surface, layout
js/glass.js        # brilho no ponteiro, encolher a navegação, detecção de refração; < 3 KB, sem dependências
index.html, cv.html, projetos.html
```

- O filtro SVG de refração (`<filter id="liquid">`) e os ícones (`<symbol>` de casa, CV, projetos, calendário, local, seta, LinkedIn e GitHub) vão inline num `<svg class="defs">` oculto em cada página. Assim o `backdrop-filter: url(#liquid)` e o `<use href="#...">` funcionam sem requisição extra, inclusive abrindo o HTML direto do disco (`file://`).
- Remover Bootstrap (CSS e JS), Font Awesome e Google Fonts de todas as páginas.
- Layout em CSS Grid/Flexbox puro, substituindo `container`/`navbar` do Bootstrap.
- O JS é **aprimoramento progressivo**: sem JS, o site funciona inteiro (navegação fixa sem encolher e sem brilho dinâmico).

### 9.2 Componentes CSS

| Classe | Descrição |
|---|---|
| `.wallpaper` | fundo fixo com blobs e ruído |
| `.glass`, `.glass--clear`, `.glass--refract` | material de vidro e variantes (§5) |
| `.surface` | cartão de conteúdo legível |
| `.tabbar`, `.tabbar__item`, `.tabbar__indicador` | navegação flutuante em cápsula |
| `.botao`, `.botao--proeminente` | botões em cápsula |
| `.chip` | link pequeno em cápsula com ícone |
| `.lista-agrupada`, `.lista-agrupada__linha` | lista do CV no estilo Ajustes |
| `.titulo-grande` | Large Title |
| `.cabecalho-secao` | título de seção em caixa alta, sticky |

### 9.3 Suporte a navegadores

| Recurso | Chrome/Edge | Safari | Firefox | Fallback |
|---|---|---|---|---|
| `backdrop-filter: blur()` | sim | sim (`-webkit-`) | sim | fundo `--surface` sólido |
| `backdrop-filter: url()` (refração) | sim | não | não | só blur + brilho |
| View Transitions entre páginas | sim | sim (18.2+) | não | navegação normal |
| `prefers-reduced-transparency` | sim | não | atrás de flag | — (também respeitar `prefers-contrast`) |

### 9.4 Orçamento de desempenho

- `backdrop-filter` custa GPU: no máximo **6 superfícies de vidro visíveis** ao mesmo tempo e nenhuma maior que a viewport.
- Wallpaper animado só com `transform`/`opacity` (nada de animar `filter` ou gradiente).
- Peso total por página: **< 100 KB** (sem fontes e sem imagens de fundo).
- Nenhuma requisição para domínios externos.
- Lighthouse: Performance ≥ 95, Accessibility ≥ 95. Sem queda perceptível de FPS ao rolar num iPhone de 3 anos atrás.

## 10. Critérios de aceite

1. As três páginas usam o novo layout: wallpaper, tab bar flutuante, cartões `.surface` e botões/chips de vidro.
2. Todo o conteúdo atual (textos do CV, projeto, links do LinkedIn/GitHub) está presente e sem alterações de texto.
3. Não há requisição a CDN nem a fonte externa (conferir na aba Network).
4. No Chrome, a navegação e os botões mostram refração nas bordas; no Safari e no Firefox, mostram o vidro com blur e brilho sem erros visuais.
5. Com `prefers-reduced-motion: reduce`, nada se move além das mudanças de estado instantâneas.
6. Com `prefers-reduced-transparency: reduce` ou `prefers-contrast: more`, não sobra nenhuma superfície translúcida.
7. Modo claro e escuro seguem o sistema e passam no contraste AA em todos os textos.
8. Em 375px de largura não há rolagem horizontal, e a tab bar fica no rodapé da tela sem cobrir conteúdo (o `main` ganha `padding-bottom` equivalente).
9. Navegar só pelo teclado alcança todos os links, com foco visível.
10. Lighthouse Accessibility ≥ 95 e Performance ≥ 95 em todas as páginas.
11. O README é atualizado: tecnologias (HTML + CSS puros, sem Bootstrap) e uma explicação do tema.

## 11. Plano de execução

1. Escrever `css/glass.css` com tokens, wallpaper e os componentes `.glass` e `.surface` (§4, §5).
2. Montar uma página de teste com o vidro sobre o wallpaper e ajustar tint, blur e brilho nos modos claro e escuro.
3. Criar o filtro SVG de refração e a detecção de suporte (§5.2).
4. Desenhar os ícones em SVG inline.
5. Reescrever `index.html` com a tab bar e o hero e validar a responsividade.
6. Migrar `cv.html` (lista agrupada) e `projetos.html` (grade de cartões).
7. Adicionar `js/glass.js` (brilho no ponteiro, encolher a navegação) e as View Transitions.
8. Remover `css/style.css` e as dependências externas; atualizar o README.
9. Rodar os critérios de aceite (§10) em Chrome, Safari (macOS e iOS) e Firefox e abrir o PR contra `master`.

## 12. Decisões em aberto

Decididas na implementação:

- **Posição da tab bar no desktop:** topo centralizado; no mobile (≤ 600px), no rodapé da tela.
- **Wallpaper:** blobs coloridos animados em CSS.
- **Brilho que segue o ponteiro:** mantido, só com mouse/trackpad e sem movimento reduzido.
- **Foto de perfil no hero:** ficou de fora; o hero continua só com texto.

Ainda em aberto:

- **Relação com o branch `redesign-anos-2000`:** os dois redesigns são alternativos. Decidir qual vai para `master` (ou se um vira tema alternativo).
