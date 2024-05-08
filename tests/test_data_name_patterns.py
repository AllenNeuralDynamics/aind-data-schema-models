"""Tests classes in data_name_patterns module"""

import unittest

from aind_data_schema_models.data_name_patterns import (
    datetime_to_name_string,
    datetime_from_name_string,
    build_data_name,
    RegexParts,
    DataRegex,
    DataLevel,
    Group,
)


class TestRegexParts(unittest.TestCase):
    """Tests methods in RegexParts class"""

    def test_patterns_success(self):
        """Tests that the regex patterns match successfully."""

        input_date = "2020-10-19"
        input_time = "08-30-59"

        self.assertRegex(input_date, RegexParts.DATE)
        self.assertRegex(input_time, RegexParts.TIME)

    def test_patterns_fail(self):
        """Tests that the regex patterns match unsuccessfully."""

        deformed_date = "10/19/2020"
        deformed_time = "8:30:59"

        self.assertNotRegex(deformed_date, RegexParts.DATE)
        self.assertNotRegex(deformed_time, RegexParts.TIME)


if __name__ == "__main__":
    unittest.main()
