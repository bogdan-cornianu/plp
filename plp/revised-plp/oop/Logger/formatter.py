__author__ = 'bogdan.cornianu'
import re
from loggerexception import LoggerException
from datetime import datetime
import inspect


class Formatter:
    def __init__(self, level, message_format, date_format):
        self.level = level
        self.msg_format = message_format
        self.date_format = date_format

    def format_message(self, message, level):
        placeholders = re.findall("%\([a-zA-Z]+\)", self.msg_format)
        result = self.msg_format
        # Get function name from which logger was called using the stack trace
        function_name = inspect.stack()[2][3]

        if "%(msg)" not in self.msg_format:
            raise LoggerException("Message format must contain at least the "
                                  "message text placeholder.")

        for item in placeholders:
            if item == "%(level)":
                result = result.replace("%(level)", level)
            elif item == "%(date)":
                result = result.replace("%(date)", self.format_date())
            elif item == "%(func)":
                result = result.replace("%(func)", function_name)
            elif item == "%(msg)":
                result = result.replace("%(msg)", message)
        return result

    def format_date(self):
        return datetime.now().strftime(self.date_format)
