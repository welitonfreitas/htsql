#
# Copyright (c) 2006-2012, Prometheus Research, LLC
# See `LICENSE` for license information, `AUTHORS` for the list of authors.
#


"""
:mod:`htsql.core.fmt`
=====================

This package implements product formatters.
"""


from . import format, html, json, tabular, text
from .format import FindRenderer
from .json import JSONRenderer, ObjRenderer
from .tabular import CSVRenderer, TSVRenderer
from .html import HTMLRenderer
from .text import TextRenderer


class FindStandardRenderer(FindRenderer):

    def get_renderers(self):
        return ([CSVRenderer, TSVRenderer, JSONRenderer,
                 HTMLRenderer, TextRenderer]
                + super(FindStandardRenderer, self).get_renderers())

