__author__ = 'bogdan.cornianu'


class ConfigReader():
    """Read a configuration file from disk."""

    def __init__(self):
        """Initial set-up."""
        self.file_name = ""
        self.file_handle = None
        self.file_map = []

    def __del__(self):
        """Release the open file handle"""
        self.file_handle.close()

    def read_config(self, file_name):
        """Read configuration from the specified file and load it into memory."""
        try:
            self.file_handle = open(file_name, "r")
            self.file_name = file_name
            self.file_map = self.file_handle.readlines()
        except IOError as error:
            print "IO error({0}): {1}".format(error.errno, error.strerror)

    def __read_property(self, property_name):
        """Find a value associated to a property."""
        if len(self.file_map) > 0:
            for line in self.file_map:
                if len(line) > 0 and line[0] != "#":
                    splitted_line = line.strip().split("=")
                    if splitted_line[0] == property_name:
                        return splitted_line[1]
            return "Property not found."
        return "No property to read."

    def get(self, prop_name):
        """Get the value for any property."""
        return str(self.__read_property(prop_name))

    def get_int(self, prop_name):
        """Get the value for prop_name as int."""
        try:
            return int(self.__read_property(prop_name))
        except ValueError as error:
            print "Invalid value: {0}".format(error.strerror)

    def get_float(self, prop_name):
        """Get the value for prop_name as float."""
        try:
            return float(self.__read_property(prop_name))
        except ValueError as error:
            print "Invalid value: {0}".format(error.strerror)

    def get_string(self, prop_name):
        """Get the value for prop_name as string."""
        try:
            return str(self.__read_property(prop_name))
        except ValueError as error:
            print "Invalid value: {0}".format(error.strerror)

    def get_boolean(self, prop_name):
        """Get the value for prop_name as boolean."""
        try:
            prop_val = self.__read_property(prop_name)

            if prop_val in ["Property not found.", "No property to read."]:
                return prop_val

            if prop_val in ["True", "False"]:
                return bool(prop_val)
            else:
                raise ValueError()
        except ValueError:
            return "Invalid value."

    def get_long(self, prop_name):
        """Get the value for prop_name as long."""
        try:
            return long(self.__read_property(prop_name))
        except ValueError as error:
            print "Invalid value: {0}".format(error.strerror)
