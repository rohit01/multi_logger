"""
Python module to print logs in console in different colors as per log level.
The program using it logs errors like any logger while performing its
execution. It can be usefull for initial development of programs as a
alternative of print statements. This logger uses the same methods to log
errors as a conventional python logger
Class extends: BaseLoggerClass
"""

import logging
from base_logger import BaseLoggerClass

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


class ConsoleLogger(BaseLoggerClass):
    """
    Class to print logs in console in different colors as per log level. The
    program using it logs errors like any logger while performing its
    execution. It can be usefull for initial development of programs as a
    alternative of print statements. This logger uses the same methods to
    log errors as a conventional python logger
    Class extends: BaseLoggerClass
    """
    def __init__(self, loglevel='INFO', enable_color=True):
        """
        Constructor to initialize ConsoleLogger object.
        """
        if type(loglevel) == type(logging.INFO):
            self.loglevel = loglevel
        else:
            self.loglevel = LOGLEVELS[loglevel]
        if enable_color == True:
            self.HEADER = '\033[95m'
            self.OKBLUE = '\033[94m'
            self.OKGREEN = '\033[92m'
            self.WARNING = '\033[93m'
            self.ERROR = '\033[91m'
            self.CRITICAL = '\033[91m\033[1m'
            self.ENDCOLOR = '\033[0m'
        else:
            self.HEADER = ''
            self.OKBLUE = ''
            self.OKGREEN = ''
            self.WARNING = ''
            self.ERROR = ''
            self.CRITICAL = ''
            self.ENDCOLOR = ''

    def debug(self, error_message, *args, **kwargs):
        """
        Logs a message with level DEBUG on this logger
        """
        if logging.DEBUG >= self.loglevel:
            final_message = self.form_log_text(error_message, *args, **kwargs)
            print self.debug_string(final_message)

    def info(self, error_message, *args, **kwargs):
        """
        Logs a message with level INFO on this logger
        """
        if logging.INFO >= self.loglevel:
            final_message = self.form_log_text(error_message, *args, **kwargs)
            print self.info_string(final_message)

    def warning(self, error_message, *args, **kwargs):
        """
        Logs a message with level WARNING on this logger
        """
        if logging.WARNING >= self.loglevel:
            final_message = self.form_log_text(error_message, *args, **kwargs)
            print self.warning_string(final_message)

    def error(self, error_message, *args, **kwargs):
        """
        Logs a message with level ERROR on this logger
        """
        if logging.ERROR >= self.loglevel:
            final_message = self.form_log_text(error_message, *args, **kwargs)
            print self.error_string(final_message)

    def exception(self, error_message, *args):
        """
        Logs a message with level ERROR on this logger. Exception info is
        added to the logging message. This method should only be called
        from an exception
        """
        if logging.ERROR >= self.loglevel:
            final_message = self.form_log_text(error_message, *args)
            print self.exception_string(final_message)

    def critical(self, error_message, *args, **kwargs):
        """
        Logs a message with level CRITICAL on this logger
        """
        if  logging.CRITICAL >= self.loglevel:
            final_message = self.form_log_text(error_message, *args, **kwargs)
            print self.critical_string(final_message)

    def debug_string(self, text):
        """
        Method to return the accepted string argument to be printed
        in debug color (white/default) & [DEBUG] tag.
        """
        return "%s[DEBUG] %s%s" % (self.HEADER, self.ENDCOLOR, text)

    def info_string(self, text):
        """
        Method to return the accepted string argument to be printed
        in info color (white/default) & [INFO] tag.
        """
        return "%s[INFO] %s%s" % (self.HEADER, self.ENDCOLOR, text)

    def warning_string(self, text):
        """
        Method to return the accepted string argument to be printed
        in warning color (Yellow) & [WARNING] tag.
        """
        return "%s[WARNING] %s%s%s%s" % (self.HEADER, self.ENDCOLOR, self.WARNING, text, self.ENDCOLOR)

    def error_string(self, text):
        """
        Method to return the accepted string argument to be printed
        in error color (Red) & [ERROR] tag.
        """
        return "%s[ERROR] %s%s%s%s" % (self.HEADER, self.ENDCOLOR, self.ERROR, text, self.ENDCOLOR)

    def exception_string(self, text):
        """
        Method to return the accepted string argument to be printed
        in error color (Red) & [EXCEPTION] tag.
        """
        return "%s[EXCEPTION] %s%s%s%s" % (self.HEADER, self.ENDCOLOR, self.ERROR, text, self.ENDCOLOR)

    def critical_string(self, text):
        """
        Method to return the accepted string argument to be printed
        in critical color (Bold Red) & [CRITICAL] tag.
        """
        return "%s[CRITICAL] %s%s%s%s" % (self.HEADER, self.ENDCOLOR, self.CRITICAL, text, self.ENDCOLOR)
