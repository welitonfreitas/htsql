#
# Copyright (c) 2006-2012, Prometheus Research, LLC
# See `LICENSE` for license information, `AUTHORS` for the list of authors.
#


from . import introspect, rulesparser
from htsql.core.addon import Addon


class TweakViewPGSQLAddon(Addon):

    name = 'tweak.view.pgsql'
    prerequisites = ['engine.pgsql']
    hint = """implement `tweak.view` for PostgreSQL"""


