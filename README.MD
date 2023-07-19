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

That's what MacWilliams matrices look like

![MacWilliams matrix of order 409 modulo 41](https://github.com/supxinfy/Diplom-slides/blob/main/examples/41.jpg)

## In case you'd like to run

We're using Manim Community v0.17.3, manim-slides v4.14.0, and Python 3.11.1 (that depends on the interpreter you've installed manim and manim-slides).

### General instructions
To run, make sure that you
<ul>
    <li>have installed manim (if not, click on your system: <a href="https://docs.manim.community/en/stable/installation/linux.html">Linux</a>, <a href="https://docs.manim.community/en/stable/installation/macos.html">MacOS</a>, or <a href="https://docs.manim.community/en/stable/installation/windows.html">Windows</a>) </li>
    <li>have installed manim-slides (again, if you haven't, follow to this <a href="https://eertmans.be/manim-slides/quickstart.html">guide</a>),</li>
</ul>
Afterwards, just find a suitable directory for cloning, and then
<ol>
    <li><pre><code>git clone https://github.com/supxinfy/Diplom-slides</code></pre></li>
    <li><pre><code>cd Diplom-slides</code></pre></li>
    These steps wouldn't work on my version of manim without solving this <a href="#russian-issue">issue</a>
    <li><pre><code>manim main.py Slide</code></pre></li>
    <li><pre><code>manim-slides Slides</pre></code></li>
</ol>

#### Russian issue

Previous steps shouldn't work fine, unless there's Cyrillic support out of the box in the version you use.
To add this, you need to do these steps.
<ol>
    <li>Install possible TeX dependencies
    <ul>
        <li>(Debian/Linux) <pre><code>sudo apt install texlive texlive-latex-extra texlive</pre></code></li>
        <li>(Mac OS) Unless you've installed some TeX with Cyrillic support, you can do <pre><code>brew install --cask mactex-no-gui</pre></code> (if you haven't done it whilst installing manim)</li>
        <li>(Windows) Frankly, I have no idea. Try it yourself.</li>
    </ul>
    </li>
    <li>Enter <pre><code>[your text editor] $(pip3 show manim | grep Location | awk '{print $2}')/manim/utils/tex.py</pre></code></li>
    <li>Add to <i>default_preamble</i> variable a line <pre><code>\usepackage{ragged2e}</pre></code> (unless it exists)</li>
    <li>Change a line <pre><code>\usepackage[english]{babel}</pre></code> to <pre><code>\usepackage[english, main=russian]{babel}</pre></code></li>
</ol>

The simpler way is to just replace your *tex.py* file with the edited one in the folder **utils** from the repository (which might cause an error due to different versions).
<ol>
    <li><pre><code>mv utils/tex.py $(pip3 show manim | grep Location | awk '{print $2}')/manim/utils/</pre></code></li>
</ol>

### Debian/Ubuntu run
Thanks to [@cowboyslick](https://github.com/cowboyslick) for full test.

Tested on Debian GNU/Linux 12 (bookworm) x86_64
- Install and setup the necessary dependencies:
  - `sudo apt-get update && sudo apt-get upgrade -y` 
  - `sudo apt-get install -y build-essential python3-dev python3-venv libcairo2-dev libpango1.0-dev ffmpeg python3-pip git texlive texlive-latex-extra texlive-lang-cyrillic`
  - `git clone https://github.com/supxinfy/Diplom-slides`
  - `cd Diplom-slides`
  - `python3 -m venv .venv`
  - `source .venv/bin/activate`
  - `python3 -m pip install manim manim-slides matplotlib`
  - `mv utils/tex.py $(pip3 show manim | grep Location | awk '{print $2}')/manim/utils`
- Render:
  This may take some time... Low quality + low spec pc (1cpu 2gb RAM) = ~7m0.891s
  - `manim --quality l main.py Slides` (`-q`, `--quality [l|m|h|p|k]` - Render quality at the following resolution framerates, respectively: 854x480 15FPS, 1280x720 30FPS, 1920x1080 60FPS, 2560x1440 60FPS, 3840x2160 60FPS, added from [here](https://docs.manim.community/en/stable/guides/configuration.html)) 
  - `manim-slides Slides`

<hr>

I implore you to bask in its magnificence, and should any inquiries or observations arise, I beseech you to graciously voice them forthwith. May you venture forth into the depths of this repository with a discerning eye, deriving both enlightenment and enjoyment from this scholarly pursuit.
Gratias tibi ago!
<p align="center"><img src="https://github.com/supxinfy/Diplom-slides/blob/main/examples/17.jpeg", alt="MacWilliams matrix of order 169 modulo 17" /></p>

## In case you'd like to run

We're using Manim Community v0.17.3, manim-slides v4.14.0, and Python 3.11.1 (that depends on the interpreter you've installed manim and manim-slides).

### General instructions
To run, make sure that you
<ul>
    <li>have installed manim (if not, click on your system: <a href="https://docs.manim.community/en/stable/installation/linux.html">Linux</a>, <a href="https://docs.manim.community/en/stable/installation/macos.html">MacOS</a>, or <a href="https://docs.manim.community/en/stable/installation/windows.html">Windows</a>) </li>
    <li>have installed manim-slides (again, if you haven't, follow to this <a href="https://eertmans.be/manim-slides/quickstart.html">guide</a>),</li>
</ul>
Afterwards, just find a suitable directory for cloning, and then
<ol>
    <li><pre><code>git clone https://github.com/supxinfy/Diplom-slides</code></pre></li>
    <li><pre><code>cd Diplom-slides</code></pre></li>
    These steps wouldn't work on my version of manim without solving this <a href="#russian-issue">issue</a>
    <li><pre><code>manim main.py Slide</code></pre></li>
    <li><pre><code>manim-slides Slides</pre></code></li>
</ol>

#### Russian issue

Previous steps shouldn't work fine, unless there's Cyrillic support out of the box in the version you use.
To add this, you need to do these steps.
<ol>
    <li>Install possible TeX dependencies
    <ul>
        <li>(Debian/Linux) <pre><code>sudo apt install texlive texlive-latex-extra texlive</pre></code></li>
        <li>(Mac OS) Unless you've installed some TeX with Cyrillic support, you can do <pre><code>brew install --cask mactex-no-gui</pre></code> (if you haven't done it whilst installing manim)</li>
        <li>(Windows) Frankly, I have no idea. Try it yourself.</li>
    </ul>
    </li>
    <li>Enter <pre><code>[your text editor] $(pip3 show manim | grep Location | awk '{print $2}')/manim/utils/tex.py</pre></code></li>
    <li>Add to <i>default_preamble</i> variable a line <pre><code>\usepackage{ragged2e}</pre></code> (unless it exists)</li>
    <li>Change a line <pre><code>\usepackage[english]{babel}</pre></code> to <pre><code>\usepackage[english, main=russian]{babel}</pre></code></li>
</ol>

The simpler way is to just replace your *tex.py* file with the edited one in the folder **utils** from the repository (which might cause an error due to different versions).
<ol>
    <li><pre><code>mv utils/tex.py $(pip3 show manim | grep Location | awk '{print $2}')/manim/utils/</pre></code></li>
</ol>

### Debian/Ubuntu run
Thanks to [@cowboyslick](https://github.com/cowboyslick) for full test.

Tested on Debian GNU/Linux 12 (bookworm) x86_64
- Install and setup the necessary dependencies:
  - `sudo apt-get update && sudo apt-get upgrade -y` 
  - `sudo apt-get install -y build-essential python3-dev python3-venv libcairo2-dev libpango1.0-dev ffmpeg python3-pip git texlive texlive-latex-extra texlive-lang-cyrillic`
  - `git clone https://github.com/supxinfy/Diplom-slides`
  - `cd Diplom-slides`
  - `python3 -m venv .venv`
  - `source .venv/bin/activate`
  - `python3 -m pip install manim manim-slides matplotlib`
  - `mv ./tex.py $(pip3 show manim | grep Location | awk '{print $2}')/manim/utils`
- Render:
  This may take some time... Low quality + low spec pc (1cpu 2gb RAM) = ~7m0.891s
  - `manim --quality l main.py Slides` (`-q`, `--quality [l|m|h|p|k]` - Render quality at the following resolution framerates, respectively: 854x480 15FPS, 1280x720 30FPS, 1920x1080 60FPS, 2560x1440 60FPS, 3840x2160 60FPS, added from [here](https://docs.manim.community/en/stable/guides/configuration.html)) 
  - `manim-slides Slides`

<hr>

I implore you to bask in its magnificence, and should any inquiries or observations arise, I beseech you to graciously voice them forthwith. May you venture forth into the depths of this repository with a discerning eye, deriving both enlightenment and enjoyment from this scholarly pursuit.
Gratias tibi ago!
<p align="center"><img src="https://github.com/supxinfy/Diplom-slides/blob/main/examples/17.jpeg", alt="MacWilliams matrix of order 169 modulo 17" /></p>