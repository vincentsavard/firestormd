import unittest

from firestormd.config.configuration import Configuration, DEFAULT_CONFIGURATION

A_DIRECTORY = "foo"
A_PORT = 12345
A_CONFIGURATION_STR = """
[videos]
directory={0}

[server]
port={1}
""".format(A_DIRECTORY, A_PORT)

AN_INCOMPLETE_CONFIGURATION_STR = """
[videos]
directory={0}
""".format(A_DIRECTORY)

class TestConfiguration(unittest.TestCase):
    def test_given_no_config_str_then_default_config_is_loaded(self):
        config = Configuration()
        self.assertEqual(config._config, DEFAULT_CONFIGURATION)

    def test_given_a_config_str_then_configuration_elements_are_set_correctly(self):
        config = Configuration(A_CONFIGURATION_STR)

        self.assertEqual(config["videos"]["directory"].value, A_DIRECTORY)
        self.assertEqual(config["server"]["port"].value, A_PORT)

    def test_given_an_incomplete_config_str_then_some_configuration_elements_are_set_to_default(self):
        config = Configuration(AN_INCOMPLETE_CONFIGURATION_STR)

        self.assertEqual(config["videos"]["directory"].value, A_DIRECTORY)
        self.assertEqual(config["server"]["port"].value, DEFAULT_CONFIGURATION["server"]["port"].value)
