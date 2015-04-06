__author__ = 'bogdan.cornianu'
from ConfigReader import ConfigReader
from LoggerException import LoggerException
from Formatter import Formatter
from os import path


class Logger:
    __log_levels__ = {
        "debug": 10,
        "info": 20,
        "warning": 30,
        "error": 40,
        "critical": 50,
    }

    def __init__(self, config):
        if path.exists(config) and path.isfile(config):
            conf = ConfigReader()
            conf.read_config(config)

            self.output = conf.get("output")
            if self.output == "file":
                self.output_file_handle = open(conf.get("output_file"), "w")
            self.level = conf.get("level")
            self.message_format = conf.get("message_format")
            self.date_format = conf.get("date_format")
            self.formatter = Formatter(self.level, self.message_format, self.date_format)
        else:
            raise IOError("Can't find configuration file.")

    def __del__(self):
        try:
            self.output_file_handle.close()
        except AttributeError:
            pass

    def set_level(self, level):
        self.level = level

    def log_message(self, msg):
        if self.output == "file":
            self.output_file_handle.write(msg + "\n")
        elif self.output == "stdout":
            print msg
        else:
            raise LoggerException("Can't output log information. Set file or stdout in logger configuration file.")

    def debug(self, msg):
        if Logger.__log_levels__["debug"] >= Logger.__log_levels__[self.level]:
            self.log_message(self.formatter.format_message(msg, "debug"))

    def info(self, msg):
        if Logger.__log_levels__["info"] >= Logger.__log_levels__[self.level]:
            self.log_message(self.formatter.format_message(msg, "info"))

    def warning(self, msg):
        if Logger.__log_levels__["warning"] >= Logger.__log_levels__[self.level]:
            self.log_message(self.formatter.format_message(msg, "warning"))

    def error(self, msg):
        if Logger.__log_levels__["error"] >= Logger.__log_levels__[self.level]:
            self.log_message(self.formatter.format_message(msg, "error"))

    def critical(self, msg):
        if Logger.__log_levels__["critical"] >= Logger.__log_levels__[self.level]:
            self.log_message(self.formatter.format_message(msg, "critical"))
