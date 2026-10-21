# Personal Portfolio Website

This repository contains the source code for the personal portfolio website of ViniciusRibSantos.

## Website Structure

The website is organized into the following HTML files:

- `index.html`: The main landing page, providing a welcome message and navigation to other sections.
- `cv.html`: Displays the Curriculum Vitae of ViniciusRibSantos, including professional experience and academic background.
- `projetos.html`: Showcases various projects developed by ViniciusRibSantos, with links to their respective repositories or live versions.

## Theme

The design follows Apple's **Liquid Glass** language (iOS 26 / macOS Tahoe): a floating capsule tab bar and glass buttons over an animated colorful wallpaper, with readable content cards, system fonts and automatic light/dark mode. On Chromium browsers, the navigation and buttons also refract what is behind them through an SVG displacement filter; other browsers get the blurred glass without refraction.

The theme respects `prefers-reduced-motion`, `prefers-reduced-transparency` and `prefers-contrast`. See [`docs/spec-redesign-liquid-glass.md`](docs/spec-redesign-liquid-glass.md) for the full spec.

## Technologies Used

- HTML
- CSS (no frameworks)
- A small vanilla JavaScript file (`js/glass.js`) for progressive enhancements

No external dependencies: no Bootstrap, icon fonts or web fonts.

## How to View the Website

To view the website, simply clone this repository and open the `index.html` file in your web browser.

Alternatively, you can access the live version of the website [here](https://viniciusribsantos.github.io/Portfolio/).
