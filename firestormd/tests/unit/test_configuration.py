import unittest

from firestormd.config.configuration import Configuration, DEFAULT_CONFIGURATION

A_DIRECTORY = "foo"
A_LIST_OF_EXTENSIONS = [".avi", ".mp4"]
A_CONFIGURATION_STR = """
[videos]
directory={0}
extensions={1}
""".format(A_DIRECTORY, ",".join(A_LIST_OF_EXTENSIONS))

AN_INCOMPLETE_CONFIGURATION_STR = """
[videos]
""".format(A_DIRECTORY)

class TestConfiguration(unittest.TestCase):
    def test_given_no_config_str_then_default_config_is_loaded(self):
        config = Configuration()
        self.assertEqual(config._config, DEFAULT_CONFIGURATION)

    def test_given_a_config_str_then_configuration_elements_are_set_correctly(self):
        config = Configuration(A_CONFIGURATION_STR)

        self.assertEqual(config["videos"]["directory"].value, A_DIRECTORY)

    def test_given_an_incomplete_config_str_then_some_configuration_elements_are_set_to_default(self):
        config = Configuration(AN_INCOMPLETE_CONFIGURATION_STR)

        self.assertEqual(config["videos"]["directory"].value, DEFAULT_CONFIGURATION["videos"]["directory"].value)

    def test_given_a_comma_delimited_value_then_it_is_correctly_parsed_as_list(self):
        config = Configuration(A_CONFIGURATION_STR)

        self.assertEqual(config["videos"]["extensions"].value, A_LIST_OF_EXTENSIONS)
