# PhD Defense Presentation

This repository contains the presentation slides for my PhD defense, created using [reveal.js](https://revealjs.com/).

## License

I designed it for personal use and do not claim it will be useful for anybody.
I nonetheless grant permission for anyone to freely use, modify, and distribute this template.

For the parts of the presentation that are based on Reveal.js, please refer to the [Reveal.js license](https://github.com/hakimel/reveal.js/blob/master/LICENSE).

## Usage

The presentation loads slides from the `/slides` directory to allow for an easier organization of the presentation.
However, because of browser restriction, this means that it is not possible to directly open [*index.html*](index.html) in your browser to view the presenation.

You need to use a local web server.

1. Clone the current repository and navigate to the root of the project:

`git clone https://github.com/ComePerrot/phd-slides.git && phd-slides`

2. Install [Node.js](https://nodejs.org) (which comes with [npm](http://npmjs.com)) with the method of your choice.

You can use mamba (or any flavor of conda you like): `mamba create -n reveal nodejs && mamba activate reveal`

You can also simply run a nix shell: `nix-shell`

3. Install the dependencies:

`npm install`

4. Serve the presentation and monitor source files for changes:

`npm start`

5. Open <http://localhost:8000> to view the presentation.

This setup also allow you to edit your own [theme](./css/theme/README.md).
## Theme

The theme used for this presentation is based on the [*white*](https://github.com/hakimel/reveal.js/blob/master/css/theme/source/white.scss) theme of Reveal.js.
It was modified to fit the CNRS style guide.

### Fonts

It uses [IBM Plex Sans](https://fonts.google.com/specimen/IBM+Plex+Sans?query=ibm) for the titles and the [Satoshi](https://www.fontshare.com/fonts/satoshi) for the text.

### Colors

The colors are defined in the [*laas.scss*](./css/theme/source/laas.scss) file.

#### CNRS Colors

The main 2 colors of the CNRS are:

- <span style="color:#ffeb6e;">■</span> **Jaune CNRS**: `#FFD700` (RGB: 255, 235, 110)
- <span style="color:#00284b;">■</span> **Bleu CNRS**: `#00284b` (RGB: 0, 40, 75)

Complementary colors can be used for variation and dynamism:

- <span style="color:#EBF0F5;">■</span> **Gris 1**: `#EBF0F5` (RGB: 235, 240, 245)
- <span style="color:#8296A5;">■</span> **Gris 2**: `#8296A5` (RGB: 130, 150, 165)
- <span style="color:#6941EB;">■</span> **Violet CNRS**: `#6941EB` (RGB: 105, 65, 235)

Additional secondary colors can be use for backgrounds or graphical emphasis:

- <span style="color:#B0EE89;">■</span> **Vert secondaire**: `#B0EE89` (RGB: 176, 238, 137)
- <span style="color:#FFBC75;">■</span> **Orange secondaire**: `#FFBC75` (RGB: 255, 188, 117)
- <span style="color:#9AE2FF;">■</span> **Bleu secondaire**: `#9AE2FF` (RGB: 154, 226, 255)

#### LAAS Colors

The LAAS two colors, in addition to **Bleu CNRS** for its branding:

- <span style="color:#62C4DD;">■</span> **Bleu LAAS**: `#62C4DD` (RGB: 98, 196, 221)
- <span style="color:#E94B57;">■</span> **Rouge LAAS**: `#E94B57` (RGB: 233, 75, 87)
