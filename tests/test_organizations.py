"""Tests classes in organizations module"""

import unittest

from aind_data_schema_models.organizations import Organization


class TestOrganization(unittest.TestCase):
    """Tests methods in Organization class"""

    def test_name_map(self):
        """Tests Organization name_map property"""

        self.assertEqual(Organization.AI, Organization.name_map["Allen Institute"])

    def test_none(self):
        """Tests that empty strings map to None"""

        self.assertEqual(Organization.LIFECANVAS.abbreviation, None)

    def test_groups(self):
        """Test that the organization groups are present"""

        self.assertIn(Organization.AI, Organization.SUBJECT_SOURCES)
        self.assertIn(Organization.AIBS, Organization.RESEARCH_INSTITUTIONS)


if __name__ == "__main__":
    unittest.main()
