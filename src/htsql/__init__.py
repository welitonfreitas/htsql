#
# Copyright (c) 2006-2012, Prometheus Research, LLC
# See `LICENSE` for license information, `AUTHORS` for the list of authors.
#


"""
:mod:`htsql`
============

:copyright: 2006-2012, Prometheus Research, LLC
:authors: Clark C. Evans <cce@clarkevans.com>,
          Kirill Simonov <xi@resolvent.net>;
          see ``AUTHORS`` file in the source distribution
          for the full list of contributors
:license: See ``LICENSE`` file in the source distribution

This package provides HTSQL, a query language for the accidental programmer.

HTSQL is implemented as a WSGI application.  To create an application, run::

    >>> from htsql import HTSQL
    >>> app = HTSQL(db)

where `db` is a connection URI, a string of the form::

    engine://username:password@host:port/database

`engine`
    The type of the database server; ``pgsql`` or ``sqlite``.

`username:password`
    Used for authentication; optional.

`host:port`
    The server address; optional.

`database`
    The name of the database; for SQLite, the path to the database file.

To execute a WSGI request, run::

    >>> app(environ, start_response)

To execute a raw HTSQL request, run::

    >>> rows = app.produce(query, **parameters)
"""


__version__ = '2.3.0+'
__copyright__ = """Copyright (c) 2006-2012, Prometheus Research, LLC"""
__license__ = None


from .core.application import Application as HTSQL


