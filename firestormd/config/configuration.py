import configparser
import os

class ConfigurationElementNotFound(Exception): pass

class ConfigurationElement:
    def __init__(self, value, type):
        self._value = type(value)
        self._type = type
        
    @property
    def value(self):
        return self._value

    @property
    def type(self):
        return self._type

    def __repr__(self):
        return "ConfigurationElement<{0}={1}>".format(self._type.__name__, self._value)

    
DEFAULT_CONFIGURATION = {
    "videos": {
        "directory": ConfigurationElement("", str),
        "driver": ConfigurationElement("omxplayer", str),
    },
}

class Configuration:
    def __init__(self, config_str=None):
        self._config_str = config_str
        self._config = None
        self._load_config()

    def __getitem__(self, section):
        return self._config[section]

    def _load_config(self):
        config_parser = configparser.ConfigParser()
        
        if self._config_str is not None:
            config_parser.read_string(self._config_str)
            self._config = self._parse_from_config_parser(config_parser)
        else:
            self._config = DEFAULT_CONFIGURATION

    def _parse_from_config_parser(self, config_parser):
        config = {}

        for section in DEFAULT_CONFIGURATION:
            for key in DEFAULT_CONFIGURATION[section]:
                if section not in config:
                    config[section] = {}

                try:
                    config[section][key] = ConfigurationElement(config_parser[section][key],
                                                                DEFAULT_CONFIGURATION[section][key].type)
                except KeyError:
                    # Key missing from config file, fallback to default
                    config[section][key] = DEFAULT_CONFIGURATION[section][key]

        return config
