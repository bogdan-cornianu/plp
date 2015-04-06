__author__ = 'bogdan.cornianu'
import re
from LoggerException import LoggerException
from datetime import datetime
import inspect


class Formatter:
    __valid_msg_tokens__ = ["date", "level", "func", "msg"]

    def __init__(self, level, msg_format, date_format):
        self.level = level
        self.msg_format = msg_format
        self.date_format = date_format

    def format_message(self, msg, level):
        placeholders = re.findall("%\([a-zA-Z]+\)", self.msg_format)
        result = self.msg_format
        # Get function name from which logger was called using the stack trace
        func_name = inspect.stack()[2][3]

        if "%(msg)" not in self.msg_format:
            raise LoggerException("Message format must contain at least the message text placeholder.")

        for item in placeholders:
            if item == "%(level)":
                result = result.replace("%(level)", level)
            elif item == "%(date)":
                result = result.replace("%(date)", self.format_date())
            elif item == "%(func)":
                result = result.replace("%(func)", func_name)
            elif item == "%(msg)":
                result = result.replace("%(msg)", msg)

        return result

    def format_date(self):
        now = datetime.now()
        return now.strftime(self.date_format)
