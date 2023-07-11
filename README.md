# Perfect Quiz Generator

A little script to generate probably more perfect quizzes than you'll ever need.

## Generating

First, run

```bash
python3 main.py
```

to generate the `tex` files in the `bin/` directory. Afterwards, run a command like

```bash
find *.tex -exec pdflatex {} \;
```

in the `bin/` directory to turn the LaTeX files into pdf's.


## What's a Perfect Quiz?

The perfect quiz is an all-or-nothing, 31 question derivatives test that you will need to complete in under 15 minutes. It has a specific format, which lends itself to be somewhat easily generated. You will get as many tries as needed until you get a perfect, but I want to get it in under at least 3 tries, so I need study resources.

Here's [500 different copies](https://drive.google.com/drive/folders/18pqYVaIQQcHNBGI7V53gPaplnY1NHM6b?usp=sharing) that I generated for my Calc class (mostly as a joke lol; I should hope you don't need 500 of them).
