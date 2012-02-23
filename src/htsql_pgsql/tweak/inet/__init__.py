#
# Copyright (c) 2006-2012, Prometheus Research, LLC
# See `LICENSE` for license information, `AUTHORS` for the list of authors.
#


from . import introspect, dump
from htsql.core.addon import Addon


class TweakINetPGSQLAddon(Addon):

    name = 'tweak.inet.pgsql'
    prerequisites = ['engine.pgsql']
    hint = """implement `tweak.inet` for PostgreSQL"""

