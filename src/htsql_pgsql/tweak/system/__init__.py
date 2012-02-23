#
# Copyright (c) 2006-2012, Prometheus Research, LLC
# See `LICENSE` for license information, `AUTHORS` for the list of authors.
#


from . import introspect
from htsql.core.addon import Addon


class TweakSystemPGSQLAddon(Addon):

    name = 'tweak.system.pgsql'
    prerequisites = ['engine.pgsql']
    hint = """implement `tweak.system` for PostgreSQL"""

