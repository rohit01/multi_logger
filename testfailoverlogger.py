#!/usr/bin/env python
"""
Python script to test MultiLogger using hard-coded values.
"""

from multilogger import MultiLogger

LOG_FILE = '/var/log/multilogger.log'
FACILITY = 'local1'

class TestMultiLogger(object):
    """
    Class to test MultiLogger using hard-coded values.
    """
    def __init__(self):
        self.logger = MultiLogger(places={'logger': True, 'email': True,
            'console': True}, loglevel='DEBUG', facility=FACILITY,
            enable_color=True)
        self.testData = {
            'DEBUG': 'Test DEBUG log',
            'INFO' : 'Test INFO log',
            'WARNING' : 'Test WARNING log',
            'WARN' : 'Test WARN log',
            'ERROR' : 'Test ERROR log',
            'EXCEPTION' : 'Test EXCEPTION log',
            'CRITICAL' : 'Test CRITICAL log'
        }

    def test_logger(self):
        """
        Method to test the MultiLogger with a data set in self.testData and
        print the logs in console
        """
        # System logger 'local6' location is '/var/log/multilogger.log'
        # Ensure you have write permission for this log file

        # Clear contents of file:
        f = open(LOG_FILE, 'w')
        f.close()

        # log test data
        self.logger.debug(self.testData['DEBUG'])
        self.logger.info(self.testData['INFO'])
        self.logger.warning(self.testData['WARNING'])
        self.logger.warn(self.testData['WARN'])
        self.logger.error(self.testData['ERROR'])
        self.logger.exception(self.testData['EXCEPTION'])
        self.logger.critical(self.testData['CRITICAL'])

        # read the contents of log file
        f = open(LOG_FILE, 'r')
        log_contents = f.read()
        f.close()

        print "\n####### Log File Contents #######\n"
        print log_contents

        # get the contents of email log
        email_body = self.logger.get_email_log()
        print "\n####### Email Body #######\n"
        print email_body


if __name__ == '__main__':
    testlogger = TestMultiLogger()
    testlogger.test_logger()
