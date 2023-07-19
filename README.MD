# Diplom-slides
Hi there. If whoever-you-are interested what is it I'll explain.
That's repository is a presentation of my talk on my bachelor's thesis.

Great appreciation to [@cowboyslick](https://github.com/cowboyslick) for a witty idea.

The idea is just to make the entire presentation through [manim-slides](https://github.com/jeertmans/manim-slides) and [manim](https://github.com/ManimCommunity/manim).
Well, due to an insanely tiny amount of time, I've made it in the simplest way possible.

## Content
Topic of my talk is "Bernstein polynomials and MacWilliams transform". Presentation made in Russian.
In case you don't know Russian, my supervisor and I have an article with the same content in English [here](https://pca-pdmi.ru/2023/files/17/Gogin-Shubin-2023.pdf).

If you don't want to read it, there is a short explanation. 
There are well-known [Bernstein polynomials](https://en.wikipedia.org/wiki/Bernstein_polynomial), which are the first example of constructive proof of [the fact](https://en.wikipedia.org/wiki/Stone–Weierstrass_theorem) that any continuous function on the compact [a, b] can be approximated by a polynomial with an arbitrary small error. Thus, it's quite useful to find new ways to compute them.

Final remark: the MacWilliams transform is a multiplication of a vector on the MacWilliams matrix. Pay attention to the fact that the MacWilliams matrix isn't the common way to call it. In the sense that people get used to [Krawtchouk matrices](https://en.wikipedia.org/wiki/Krawtchouk_matrices) as a proper term. The reason is just a tradition of my supervisor.

<hr>
That's what MacWilliams matrices look like

![MacWilliams matrix of order 409 modulo 41](https://github.com/supxinfy/Diplom-slides/blob/main/examples/41.jpg)

## In case you'd like to run

We're using Manim Community v0.17.3, manim-slides v4.14.0, and Python 3.11.1 (that depends on the interpreter you've installed manim and manim-slides).

### General instructions
To run, make sure that you
<ul>
    <li>have installed manim (if not, click on your system: [Linux][manim-linux], [MacOS][manim-macos], [Windows][manim-windows]) </li>
    <li>have installed manim-slides (again, if you haven't, follow to this [guide](https://eertmans.be/manim-slides/quickstart.html)),</li>
</ul>
Afterwards, just find a suitable directory for cloning, and then
<ol>
    <li>`git clone https://github.com/supxinfy/Diplom-slides`</li>
    <li>`cd Diplom-slides`</li>
    These steps wouldn't work on my version of manim without solving this [issue](#russian-issue)
    <li>`manim main.py Slides`</li>
    <li>`manim-slides Slides`</li>
</ol>

[manim-linux] : https://docs.manim.community/en/stable/installation/linux.html
[manim-macos] : https://docs.manim.community/en/stable/installation/macos.html
[manim-windows] : https://docs.manim.community/en/stable/installation/windows.html

#### Russian issue

Previous steps shouldn't work fine, unless there's Cyrillic support out of the box in the version you use.
To add this, you need to do these steps.
<ol>
    <li>Install possible TeX dependencies
    <ul>
        <li>(Debian/Linux) `sudo apt install texlive texlive-latex-extra texlive`</li>
        <li>(Mac OS) Unless you've installed some TeX with Cyrillic support, you can do `brew install --cask mactex-no-gui` (if you haven't done it in whilst installing manim)</li>
        <li>(Windows) Frankly, I have no idea. Try it yourself.</li>
    </ul>
    </li>
    <li>Enter `[your text editor] $(pip3 show manim | grep Location | awk '{print $2}')/manim/utils/tex.py`</li>
    <li>Add to *default_preamble* variable a line `\usepackage{ragged2e}` (unless it exists)</li>
    <li>Change a line `\usepackage[english]{babel}` to `\usepackage[english, main=russian]{babel}`</li>
</ol>

The simpler way is to just replace your *tex.py* file with the edited one in the folder **utils** from the repository (which might cause an error due to different versions).
<ol>
    <li>mv utils/tex.py $(pip3 show manim | grep Location | awk '{print $2}')/manim/utils/</li>
</ol>

### Ubunty/Debian
Thanks to [@cowboyslick](https://github.com/cowboyslick) for full installation process.
- `sudo apt-get update && sudo apt-get upgrade` 
- `sudo apt-get install texlive texlive-latex-extra texlive`
- `pip3 install manim`
- `pip3 install manim-slides`
- `git clone https://github.com/supxinfy/Diplom-slides`
- `cd Diplom-slides`
- `mv ./tex.py $(pip3 show manim | grep Location | awk '{print $2}')/manim/utils` ([explanation](#russian-issue))
- `manim main.py Slides`
- `manim-slides Slides`

