class BaseLoggerClass(object):
    """
    class to be inherited by custom loggers. This class serves as a standard
    for the methods that should be overriding by the child classes.
    There is no logic/functionality in this class.
    """

    def __init__(self, loglevel=None):
        pass

    def debug(self, error_message, *args, **kwargs):
        """
        Logs a message with level DEBUG on this logger
        """
        pass

    def info(self, error_message, *args, **kwargs):
        """
        Logs a message with level INFO on this logger
        """
        pass

    def warning(self, error_message, *args, **kwargs):
        """
        Logs a message with level WARNING on this logger
        """
        pass

    def error(self, error_message, *args, **kwargs):
        """
        Logs a message with level ERROR on this logger
        """
        pass

    def exception(self, error_message, *args):
        """
        Logs a message with level ERROR on this logger. Exception info is
        added to the logging message. This method should only be called
        from an exception
        """
        pass

    def critical(self, error_message, *args, **kwargs):
        """
        Logs a message with level CRITICAL on this logger
        """
        pass

    def form_log_text(self, error_message, *args, **kwargs):
        """
        Common method across all child loggers for forming a string using
        error_message, *args & **kwargs
        TODO: kwargs for string formation not added
        """
        messages = [error_message]
        messages.extend(args)
        final_message = ', '.join(messages)
        return final_message
