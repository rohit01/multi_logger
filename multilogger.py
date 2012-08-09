"""
Python module to facilitate logging at three places simultaneously:
1. System Logger (rsyslog)
2. Logger mails (Attaching debug logs)
3. System console
+++ Logging in other areas if required (future additions)
"""

import logging

from logging.handlers import SysLogHandler
from base_logger import BaseLoggerClass
from consolelogger import ConsoleLogger
from emaillogger import EmailLogger


LOGLEVELS = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARN': logging.WARNING,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'EXCEPTION': logging.ERROR,
    'CRITICAL': logging.CRITICAL,
    'FATAL': logging.FATAL,
}


def get_logger(places={'logger': True, 'email': True, 'console': False},
            loglevel='INFO', facility=None, enable_color=True):
    """
    Method to create a MultiLogger object using the arguments and
    return the same
    """
    logger = MultiLogger(places, loglevel, facility, enable_color)
    return logger


class MultiLogger(BaseLoggerClass):
    """
    class to facilitate logging at three places simultaneously:
    1. System Logger (rsyslog)
    2. Multi mails (Attaching debug logs)
    3. System console
    +++ Logging in other areas if required (future additions)
    Init arguments:
        places: dictionary with string keys & boolean values to
                enable/disable logging in different places
        facility: used by system logger
        loglevel: Log Level for logs. Default: 'INFO'
        enable_color: used by console logger. Enables color output
    """
    def __init__(self, places={'logger': True, 'email': True, 'console': False},
            loglevel='INFO', facility=None, enable_color=True):
        """
        Constructor to initialize MultiLogger object.
        """
        if type(loglevel) == type(logging.INFO):
            self.loglevel = loglevel
        else:
            self.loglevel = LOGLEVELS[loglevel]
        self.log_in_logger = bool(places['logger'])
        self.log_in_email = bool(places['email'])
        self.log_in_console = bool(places['console'])
        if self.log_in_logger == True:
            self.set_system_logger(self.loglevel, facility)
        else:
            self.system_logger = None
        if self.log_in_email == True:
            self.set_email_logger(self.loglevel)
        else:
            self.email_logger = None
        if self.log_in_console == True:
            self.set_console_logger(self.loglevel, enable_color)
        else:
            self.console_logger = None
        self.highest_level_reported = None

    def set_system_logger(self, loglevel, facility=None):
        """
        Method to create a System Logger object using the arguments and
        set the same as property 'system_logger'
        """
        logger = logging.getLogger()
        logger.setLevel(loglevel)
        if facility:
            syslog = SysLogHandler(address='/dev/log', facility=facility)
            formatter = logging.Formatter('%(name)s: %(levelname)s %(message)r')
            syslog.setFormatter(formatter)
            logger.addHandler(syslog)
        self.system_logger = logger

    def set_email_logger(self, loglevel):
        """
        Method to create a EmailLogger object using the arguments and
        set the same as property 'email_logger'
        """
        self.email_logger = EmailLogger(loglevel)

    def set_console_logger(self, loglevel, enable_color):
        """
        Method to create a ConsoleLogger object using the arguments and
        set the same as property 'console_logger'
        """
        self.console_logger = ConsoleLogger(loglevel)

    def get_email_log(self):
        """
        Return: The logs which can be appended in email
        """
        if self.log_in_email == True:
            return self.email_logger.get_email_log()
        return ''

    def debug(self, error_message, *args, **kwargs):
        """
        Logs a message with level DEBUG on this logger
        """
        if logging.DEBUG >= self.loglevel:
            if self.log_in_logger:
                self.system_logger.debug(error_message, *args, **kwargs)
            if self.log_in_email:
                self.email_logger.debug(error_message, *args, **kwargs)
            if self.log_in_console:
                self.console_logger.debug(error_message, *args, **kwargs)
        if ((self.highest_level_reported == None) or
            (self.highest_level_reported < logging.DEBUG)):
            self.highest_level_reported = logging.DEBUG

    def info(self, error_message, *args, **kwargs):
        """
        Logs a message with level INFO on this logger
        """
        if logging.INFO >= self.loglevel:
            if self.log_in_logger:
                self.system_logger.info(error_message, *args, **kwargs)
            if self.log_in_email:
                self.email_logger.info(error_message, *args, **kwargs)
            if self.log_in_console:
                self.console_logger.info(error_message, *args, **kwargs)
        if ((self.highest_level_reported == None) or
            (self.highest_level_reported < logging.INFO)):
            self.highest_level_reported = logging.INFO

    def warning(self, error_message, *args, **kwargs):
        """
        Logs a message with level WARNING on this logger
        """
        if logging.WARNING >= self.loglevel:
            if self.log_in_logger:
                self.system_logger.warning(error_message, *args, **kwargs)
            if self.log_in_email:
                self.email_logger.warning(error_message, *args, **kwargs)
            if self.log_in_console:
                self.console_logger.warning(error_message, *args, **kwargs)
        if ((self.highest_level_reported == None) or
            (self.highest_level_reported < logging.WARNING)):
            self.highest_level_reported = logging.WARNING

    def warn(self, error_message, *args, **kwargs):
        """
        Logs a message with level WARNING on this logger
        """
        self.warning(error_message, *args, **kwargs)

    def error(self, error_message, *args, **kwargs):
        """
        Logs a message with level ERROR on this logger
        """
        if logging.ERROR >= self.loglevel:
            if self.log_in_logger:
                self.system_logger.error(error_message, *args, **kwargs)
            if self.log_in_email:
                self.email_logger.error(error_message, *args, **kwargs)
            if self.log_in_console:
                self.console_logger.error(error_message, *args, **kwargs)
        if ((self.highest_level_reported == None) or
            (self.highest_level_reported < logging.ERROR)):
            self.highest_level_reported = logging.ERROR

    def exception(self, error_message, *args):
        """
        Logs a message with level ERROR on this logger. Exception info is
        added to the logging message. This method should only be called
        from an exception
        """
        if logging.ERROR >= self.loglevel:
            if self.log_in_logger:
                self.system_logger.exception(error_message, *args)
            if self.log_in_email:
                self.email_logger.exception(error_message, *args)
            if self.log_in_console:
                self.console_logger.exception(error_message, *args)
        if ((self.highest_level_reported == None) or
            (self.highest_level_reported < logging.ERROR)):
            self.highest_level_reported = logging.ERROR

    def critical(self, error_message, *args, **kwargs):
        """
        Logs a message with level CRITICAL on this logger
        """
        if logging.CRITICAL >= self.loglevel:
            if self.log_in_logger:
                self.system_logger.critical(error_message, *args, **kwargs)
            if self.log_in_email:
                self.email_logger.critical(error_message, *args, **kwargs)
            if self.log_in_console:
                self.console_logger.critical(error_message, *args, **kwargs)
        if ((self.highest_level_reported == None) or
            (self.highest_level_reported < logging.CRITICAL)):
            self.highest_level_reported = logging.CRITICAL

