"""Tests classes in organizations module"""

import unittest

from aind_data_schema_models.organizations import Organizations


class TestOrganization(unittest.TestCase):
    """Tests methods in Organization class"""

    def test_name_map(self):
        """Tests Organization name_map property"""

        self.assertEqual(Organizations.AllenInstitute, Organizations._name_map["Allen Institute"])


if __name__ == "__main__":
    unittest.main()
