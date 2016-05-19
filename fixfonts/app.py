"""This module contains the main entrypoint for use in the package's command line tool.
"""
import argparse
import os
import fontforge
from collections import Counter


def main():
    """Main entrypoint where the magic happens.
    """
    parser = argparse.ArgumentParser(description="Converts fonts to fixed-width fonts.")
    parser.add_argument("-o", "--output", help="Output folder", default="output")
    parser.add_argument("input", help="Input font file", nargs="+")
    args = parser.parse_args()


    # Would be better to catch the exception on the .open() call but fontforge insists on displaying its own message...
    for filename in args.input:
        if not os.path.exists(filename):
            print("\033[31mError:\033[0m File \"{}\" not found.".format(filename))
            return
    if not os.path.exists(args.output):
        os.makedirs(args.output)

    # Display pretty title
    print("\033[1m\033[4mFixed-width Font Fixer\033[0m\n")
    print("Processing {} files...".format(len(args.input)))

    for filename in args.input:
        output_filename = os.path.join(args.output, "Fixed.{}".format(os.path.basename(filename)))
        print("Converting:\t\033[1m{}\033[0m to\n\t\t\033[1m{}\033[0m".format(filename, os.path.realpath(output_filename)))

        # Super complex font library magic here
        font = fontforge.open(filename)
        widths = Counter([glyph.width for glyph in font.glyphs()])

        # Pick the most common width because almost all of them will be the same in any "monospace but not Windows
        # fixed-width compatible" font.
        correct_width = widths.most_common()[0][0]

        # Put any non-compliant glyphs in their place
        bad_glyphs = [glyph for glyph in font.glyphs() if glyph.width != correct_width]
        for glyph in bad_glyphs:
            glyph.width = correct_width
        print("\t\033[1mFixing:\033[0m {}...".format(", ".join([glyph.glyphname for glyph in bad_glyphs])))

        font.generate(output_filename)

if __name__ == "__main__":
    main()
