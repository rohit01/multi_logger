"""
Python module to store logs in string format while the program using it
performs its execution. This log can be appended in email body or attached
as a file for dubug purpose.
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

class EmailLogger(BaseLoggerClass):
    """
    Class to store logs in string format while the program using it performs
    its execution. This log can be appended in email body or attached as a
    file for dubug purpose.
    Class extends: BaseLoggerClass
    """
    def __init__(self, loglevel='INFO'):
        """
        Constructor to initialize EmailLogger object.
        """
        if type(loglevel) == type(logging.INFO):
            self.loglevel = loglevel
        else:
            self.loglevel = LOGLEVELS[loglevel]
        self.loglevel = loglevel
        self.log_body = ''
        self.set_log_header()

    def set_log_header(self, header=None):
        """
        Method to set the log header which appears before the logs are
        appended in email
        """
        if header == None:
            self.log_header = "\n################EMAIL LOGS################\n"
        else:
            self.log_header = header

    def get_email_log(self):
        """
        Return: log_header + log_body.
        These logs can be appended in email
        """
        if self.log_header == None:
            self.log_header = ''
        if self.log_body == None:
            self.log_body = ''
        return ''.join([self.log_header, self.log_body])

    def reset_email_log(self):
        """
        Method to reset email logs (self.log_body)
        """
        self.log_body = ''

    def debug(self, error_message, *args, **kwargs):
        """
        Logs a message with level DEBUG on this logger
        """
        if logging.DEBUG >= self.loglevel:
            final_message = self.form_log_text(error_message, *args, **kwargs)
            self.log_body = '\n'.join([self.log_body, self.debug_string(final_message)])

    def info(self, error_message, *args, **kwargs):
        """
        Logs a message with level INFO on this logger
        """
        if logging.INFO >= self.loglevel:
            final_message = self.form_log_text(error_message, *args, **kwargs)
            self.log_body = '\n'.join([self.log_body, self.info_string(final_message)])

    def warning(self, error_message, *args, **kwargs):
        """
        Logs a message with level WARNING on this logger
        """
        if logging.WARNING >= self.loglevel:
            final_message = self.form_log_text(error_message, *args, **kwargs)
            self.log_body = '\n'.join([self.log_body, self.warning_string(final_message)])

    def error(self, error_message, *args, **kwargs):
        """
        Logs a message with level ERROR on this logger
        """
        if logging.ERROR >= self.loglevel:
            final_message = self.form_log_text(error_message, *args, **kwargs)
            self.log_body = '\n'.join([self.log_body, self.error_string(final_message)])

    def exception(self, error_message, *args):
        """
        Logs a message with level ERROR on this logger. Exception info is
        added to the logging message. This method should only be called
        from an exception
        """
        if logging.ERROR >= self.loglevel:
            final_message = self.form_log_text(error_message, *args)
            self.log_body = '\n'.join([self.log_body, self.exception_string(final_message)])

    def critical(self, error_message, *args, **kwargs):
        """
        Logs a message with level CRITICAL on this logger
        """
        if logging.CRITICAL >= self.loglevel:
            final_message = self.form_log_text(error_message, *args, **kwargs)
            self.log_body = '\n'.join([self.log_body, self.critical_string(final_message)])

    def debug_string(self, text):
        """
        Method to return the accepted string argument to be printed
        in info color (white/default) & [DEBUG] tag.
        TODO: Coloring text in email not done.
        """
        return "[DEBUG] %s" % (text)

    def info_string(self, text):
        """
        Method to return the accepted string argument to be printed
        in info color (white/default) & [INFO] tag.
        TODO: Coloring text in email not done.
        """
        return "[INFO] %s" % (text)

    def warning_string(self, text):
        """
        Method to return the accepted string argument to be printed
        in warning color (Yellow) & [WARNING] tag.
        TODO: Coloring text in email not done.
        """
        return "[WARNING] %s" % (text)

    def error_string(self, text):
        """
        Method to return the accepted string argument to be printed
        in error color (Red) & [ERROR] tag.
        TODO: Coloring text in email not done.
        """
        return "[ERROR] %s" % (text)

    def exception_string(self, text):
        """
        Method to return the accepted string argument to be printed
        in error color (Red) & [EXCEPTION] tag.
        TODO: Coloring text in email not done.
        """
        return "[EXCEPTION] %s" % (text)

    def critical_string(self, text):
        """
        Method to return the accepted string argument to be printed
        in critical color (Bold Red) & [CRITICAL] tag.
        TODO: Coloring text in email not done.
        """
        return "[CRITICAL] %s" % (text)
