# Fix Fixed-Pitch Fonts

This tool is a tiny script that intends to solve the problem of monospace fonts, programming oriented fonts in
particular, being unuseable in Windows tools such as the command prompt, PuTTY, etc., due to small numbers of glyphs
with inconsistent widths. See [this article](https://support.microsoft.com/en-us/kb/247815) from Microsoft for details.

## Installation

The Python library for [fontforge](https://github.com/fontforge/fontforge) is used to edit the font files. Installation
can be non trivial for some platforms, but see your platform's packages for precompiled versions. For example, Ubuntu
has support via `apt-get install python-fontforge`.

After that, simply type `python setup.py install` and the and the **fixfonts** tool will be available.

## Usage

Here is the usage output from **fixfonts**:

```bash
usage: fixfonts [-h] [-o OUTPUT] input [input ...]

Converts fonts to fixed-width fonts.

positional arguments:
  input                 Input font file

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output folder
```

For example:

```bash
$ fixfonts --output newfiles *.ttf
```

will convert every file in the current directory and place the new ones into the "newfiles" directory.
