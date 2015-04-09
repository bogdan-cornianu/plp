__author__ = 'bogdan.cornianu'


class ConfigReader():
    def __init__(self, file_name):
        with open(file_name, "r") as f:
            self.config_lines = map(lambda l: l.strip(), f.readlines())

        self.file_map = {}
        for line in self.config_lines:
            if "=" in line:
                splitted_line = line.split("=")
                self.file_map[splitted_line[0]] = splitted_line[1]

    def get_value_for(self, property_name):
        if property_name in self.file_map:
            return self.file_map[property_name]
        return "Property not found."

    def get(self, prop_name):
        return str(self.get_value_for(prop_name))

    def get_int(self, prop_name):
        try:
            return int(self.get_value_for(prop_name))
        except ValueError:
            return "Invalid value."

    def get_float(self, prop_name):
        try:
            return float(self.get_value_for(prop_name))
        except ValueError:
            return "Invalid value."

    def get_string(self, prop_name):
        try:
            return str(self.get_value_for(prop_name))
        except ValueError:
            return "Invalid value."

    def get_boolean(self, prop_name):
        try:
            prop_val = self.get_value_for(prop_name)
            if prop_val == "Property not found.":
                return prop_val
            if prop_val in ["True", "False"]:
                return bool(prop_val)
            raise ValueError()
        except ValueError:
            return "Invalid value."

    def get_long(self, prop_name):
        try:
            return long(self.get_value_for(prop_name))
        except ValueError:
            return "Invalid value."
