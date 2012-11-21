#
# Copyright (c) 2006-2012, Prometheus Research, LLC
#


from htsql.core.connect import (Connect, Scramble, Unscramble, UnscrambleError,
        DBError)
from htsql.core.adapter import adapt
from htsql.core.context import context
from htsql.core.domain import (BooleanDomain, TextDomain, EnumDomain,
        TimeDomain)
import MySQLdb, MySQLdb.connections
import datetime


class Cursor(MySQLdb.connections.Connection.default_cursor):

    _defer_warnings = True


class MySQLError(DBError):
    """
    Raised when a database error occurred.
    """


class ConnectMySQL(Connect):

    def open(self):
        # Note: `with_autocommit` is ignored.
        addon = context.app.htsql
        parameters = {}
        parameters['db'] = addon.db.database
        if addon.db.host is not None:
            parameters['host'] = addon.db.host
        if addon.db.port is not None:
            parameters['port'] = addon.db.port
        if addon.db.username is not None:
            parameters['user'] = addon.db.username
        if addon.db.password is not None:
            parameters['passwd'] = addon.db.password
        if addon.password is not None:
            parameters['passwd'] = addon.password
        parameters['use_unicode'] = True
        parameters['charset'] = 'utf8'
        parameters['cursorclass'] = Cursor
        connection = MySQLdb.connect(**parameters)
        return connection


class UnscrambleMySQLError(UnscrambleError):

    def __call__(self):
        # If we got a DBAPI exception, generate our error out of it.
        if isinstance(self.error, MySQLdb.Error):
            message = str(self.error)
            error = MySQLError(message)
            return error

        # Otherwise, let the superclass return `None`.
        return super(UnscrambleMySQLError, self).__call__()


class UnscrambleMySQLBoolean(Unscramble):

    adapt(BooleanDomain)

    @staticmethod
    def convert(value):
        if value is None:
            return None
        return (value != 0)


class UnscrambleMySQLText(Unscramble):

    adapt(TextDomain)

    @staticmethod
    def convert(value):
        if isinstance(value, str):
            value = value.decode('utf-8')
        return value


class UnscrambleMySQLEnum(Unscramble):

    adapt(EnumDomain)

    def convert(self, value):
        if isinstance(value, str):
            value = value.decode('utf-8')
        if value not in self.domain.labels:
            value = None
        return value


class UnscrambleMySQLTime(Unscramble):

    adapt(TimeDomain)

    @staticmethod
    def convert(value):
        if isinstance(value, datetime.timedelta):
            if value.days != 0:
                value = None
            else:
                value = (datetime.datetime(2001,1,1) + value).time()
        return value


