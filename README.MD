# Diplom-slides
Hi there. If whatever-you-are interested what is it I'll explain.
That's rep is a presentation of my talk on my bachelor's thesis.

Great appreciation to [@cowboyslick](https://github.com/cowboyslick) for a witty idea.

The idea is just to make the entire presentation through [manim-slides](https://github.com/jeertmans/manim-slides) and [manim](https://github.com/ManimCommunity/manim).
Well, due to an insanely tiny amount of time, I've made it in the simplest way possible.

## Content
Topic of my talk is "Bernstein polynomials and MacWilliams transform". Presentation made in Russian.
In case you don't know Russian, my supervisor and I have an article with the same content in English [here](https://pca-pdmi.ru/2023/files/17/Gogin-Shubin-2023.pdf).

If you don't want to read it, there is a short explanation. 
There're well-known [Bernstein polynomials](https://en.wikipedia.org/wiki/Bernstein_polynomial), which is the first example of constructive proof of [the fact](https://en.wikipedia.org/wiki/Stone–Weierstrass_theorem) that any continuous function on the compact [a, b] can be approximated by a polynomial with an arbitrary small error. Thus, it's quite useful to find new ways to compute them.

Final remark: the MacWilliams transform is a multiplication of a vector on the MacWilliams matrix. Pay attention to the fact that the MacWilliams matrix isn't the common way to call it. In the sense that people get used to [Krawtchouk matrices](https://en.wikipedia.org/wiki/Krawtchouk_matrices) as a proper term. The reason is just a tradition of my supervisor.

That's what MacWilliams matrices look like

![MacWilliams matrix of order 409 modulo 41](https://github.com/supxinfy/Diplom-slides/blob/main/examples/41.jpg)

## In case you'd like to run
### Debian/Ubuntu
- Install and setup necessary depedencies:
  - `sudo apt-get update && sudo apt-get upgrade -y` 
  - `sudo apt-get install -y build-essential python3-dev python3.11-venv libcairo2-dev libpango1.0-dev ffmpeg python3-pip git texlive texlive-latex-extra texlive-lang-cyrillic`
  - `git clone https://github.com/supxinfy/Diplom-slides`
  - `cd Diplom-slides`
  - `python3 -m venv .venv`
  - `source .venv/bin/activate`
  - `python3 -m pip install manim manim-slides matplotlib`
  - `mv ./tex.py $(pip3 show manim | grep Location | awk '{print $2}')/manim/utils`
- Render:
  This may take some time... Low quality + low spec pc (1cpu 2gb RAM) = ~7m0.891s
  - `manim --quality l main.py Slides` (`-q`, `--quality [l|m|h|p|k]` - Render quality at the follow resolution framerates, respectively: 854x480 15FPS, 1280x720 30FPS, 1920x1080 60FPS, 2560x1440 60FPS, 3840x2160 60FPS) 
  - `manim-slides Slides`
