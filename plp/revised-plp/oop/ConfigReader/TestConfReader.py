__author__ = 'bogdan.cornianu'
from ConfigReader import ConfigReader


config = ConfigReader()
config.read_config("../../res/test.cfg")

print config.get("name")
print config.get_string("name")
print config.get_int("some_int")
print config.get_float("some_float")
print config.get_long("some_long")
print config.get_boolean("some_bool")

print config.get_boolean("some_int")
print config.get_boolean("some_nonexistent_property")