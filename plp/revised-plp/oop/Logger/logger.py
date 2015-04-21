from configreader import ConfigReader
from loggerexception import LoggerException
from formatter import Formatter
from os import path


class Logger(object):
    def __init__(self, config_file):
        if path.exists(config_file) and path.isfile(config_file):
            conf = ConfigReader(config_file)
            self.output = conf.get("output")
            self.output_file = conf.get("output_file")
            self.level = conf.get("level")
            self.__log_levels = {
                "debug": 10,
                "info": 20,
                "warning": 30,
                "error": 40,
                "critical": 50,
                }
            self.message_format = conf.get("message_format")
            self.date_format = conf.get("date_format")
            self.formatter = Formatter(
                self.level, self.message_format, self.date_format)
        else:
            raise IOError("Can't find configuration file.")

    @property
    def log_levels(self):
        return self.__log_levels

    def set_level(self, level):
        self.level = level

    def log_message(self, message):
        if self.output == "file":
            with open(self.output_file, "a") as f:
                f.write(message + "\n")
        elif self.output == "stdout":
            print message
        else:
            raise LoggerException("Can't output log information. Set file or "
                                  "stdout in logger configuration file.")

    def should_log(self, level):
        return self.log_levels[level] >= self.log_levels[self.level]

    def debug(self, message):
        if self.should_log("debug"):
            self.log_message(self.formatter.format_message(message, "debug"))

    def info(self, message):
        if self.should_log("info"):
            self.log_message(self.formatter.format_message(message, "info"))

    def warning(self, message):
        if self.should_log("warning"):
            self.log_message(self.formatter.format_message(message, "warning"))

    def error(self, message):
        if self.should_log("error"):
            self.log_message(self.formatter.format_message(message, "error"))

    def critical(self, message):
        if self.should_log("critical"):
            self.log_message(self.formatter.format_message(message,
                                                           "critical"))
