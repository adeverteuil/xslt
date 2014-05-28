#!/usr/bin/python3

import sys
import argparse

import lxml.etree


def main():
    options = process_args()
    input_tree = lxml.etree.parse(options.input)
    transformer = lxml.etree.XSLT(lxml.etree.parse(options.stylesheet))
    result_tree = transformer(input_tree)
    result_tree.write(
        options.output,
        encoding="ISO-8859-1",
        pretty_print=options.pretty_print,
        )


class StylesheetNameAction(argparse.Action):
    """Argument parser action to determine the name of the file to open."""

    def __call__(self, parser, namespace, values, option_string=None):
        """Process the command line option.
        
        If the stylesheet is not specified, take the input file name, remove
        the extension, and add the .xsl extension.

        Otherwise, open the file name provided as a parameter.
        """

        if not values:
            try:
                # Extract XSL filename from xml-stylesheet processing instruction.
                doc = lxml.etree.parse(namespace.input)
                namespace.input.seek(0)
                pi = doc.xpath("/processing-instruction('xml-stylesheet')")[0]
                if isinstance(pi, lxml.etree._XSLTProcessingInstruction):
                    namespace.stylesheet = open(pi.attrib['href'], "rb")
                else:
                    raise TypeError
            except (IndexError, TypeError):
                # Remove the extension from the input file
                # and add the .xsl extension.
                basename = namespace.input.name.rsplit(".", maxsplit=1)[0]
                namespace.stylesheet = open(basename+".xsl", "rb")
        else:
            # Pass the received option as is.
            namespace.stylesheet = values


def process_args(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="Transform XML with XSL.")
    parser.add_argument(
        "input",
        type=argparse.FileType("rb"),
        help="Name of an XML file",
        )
    parser.add_argument(
        "output",
        type=argparse.FileType("wb"),
        help="Name of an XML file (will be overwritten)",
        )
    parser.add_argument(
        "stylesheet",
        type=argparse.FileType("rb"),
        nargs="?",
        default=None,
        action=StylesheetNameAction,
        help=(
            "Name of an XSLT file "
            "(default try finding xml-stylesheet processing instruction, "
            "otherwise same as input but with .xsl extension)"
            ),
        )
    parser.add_argument(
        "-p", "--pprint",
        action="store_true",
        default=False,
        dest="pretty_print",
        help="Nicely indent resulting XML",
        )
    return parser.parse_args(args)


if __name__ == "__main__":
    main()
