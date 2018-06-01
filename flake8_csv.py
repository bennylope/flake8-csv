# encoding: utf-8

"""
Flake8 plugin for CSV formatted reporting::

    flake8 --format=csv

"""

import csv
import sys
from collections import OrderedDict

from flake8.formatting import base
from flake8.style_guide import Violation
from pkg_resources import DistributionNotFound, get_distribution

try:
    from typing import Tuple
except ImportError:
    Tuple = None

__author__ = "Ben Lopatin"
__license__ = "MIT"

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass


category_complexity = "Complexity"
category_bug = "Bug Risk"
category_style = "Style"
category_clarity = "Clarity"
category_compatibility = "Compatibility"


error_classes = OrderedDict(
    [
        ("E722", category_bug),
        ("C9", category_complexity),
        ("W6", category_compatibility),
        ("E7", category_clarity),
        ("E9", category_bug),
        ("F", category_bug),
        ("E", category_style),
        ("W", category_style),
    ]
)


def error_category(error_code):
    for code in [error_code, error_code[:2], error_code[:1]]:
        try:
            return error_classes[code]

        except:
            continue

    return category_bug


class CategorizedCSVFormatter(base.BaseFormatter):
    """Formatter for CSV reporting with categorization"""

    columns = [
        "Category", "Code", "Description", "Filename", "Line", "Column", "Code context"
    ]

    def start(self):
        """Prepare the formatter to receive input.

        This defaults to initializing :attr:`output_fd` if :attr:`filename`
        """
        if self.filename:
            self.output_fd = open(self.filename, "a")

        self.csv_writer = csv.writer(
            self.output_fd or sys.stdout, quoting=csv.QUOTE_ALL
        )
        self.csv_writer.writerow(self.columns)

    def after_init(self):
        sys.stdout.write(self.options)

    def format(self, error):
        # type: (Violation) -> Tuple
        return (
            error_category(error.code),
            error.code,  # code
            error.text,  # descript
            error.filename,  # filename
            error.line_number,  # line
            error.column_number,  # column
            "`{}`".format(error.physical_line),  # body
        )

    def handle(self, error):
        # type: (Violation) -> None
        """Handle an error reported by Flake8."""
        line = self.format(error)
        self.csv_writer.writerow(line)


class CSVFormatter(CategorizedCSVFormatter):
    """CSV formatter excluding categorization"""

    columns = ["Code", "Description", "Filename", "Line", "Column", "Code context"]

    def format(self, error):
        return super(CSVFormatter, self).format(error)[1:]
