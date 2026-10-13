"""Tests classes in organizations module"""

import unittest

from aind_data_schema_models.organizations import Organization
from typing import get_args


class TestOrganization(unittest.TestCase):
    """Tests methods in Organization class"""

    def test_name_map(self):
        """Tests Organization name_map property"""

        self.assertEqual(Organization.AI, Organization.name_map["Allen Institute"])

    def test_none(self):
        """Tests that empty strings map to None"""

        self.assertEqual(Organization.LIFECANVAS.abbreviation, None)

    def test_from_none(self):
        """Test that you can't get an organization from None"""

        self.assertEqual(Organization.from_abbreviation(None), None)

    def test_groups(self):
        """Test that the organization groups are present"""

        union_types = get_args(Organization.SUBJECT_SOURCES.__origin__)
        self.assertTrue(any(isinstance(Organization.AI, t) for t in union_types))

        union_types = get_args(Organization.RESEARCH_INSTITUTIONS.__origin__)
        self.assertTrue(any(isinstance(Organization.AIBS, t) for t in union_types))


    def test_added_main_organizations(self):
        """Test the project organizations backported for v0.8."""

        expected_funders = {
            "Aligning Science Across Parkinson's",
            "Esther A. & Joseph Klingenstein Fund",
            "G. Harold & Leila Y. Mathers Foundation",
            "Helen Hay Whitney Foundation",
            "Klingenstein Third Generation Foundation",
            "Life Sciences Research Foundation",
            "McKnight Brain Research Foundation",
            "McKnight Foundation",
            "National Institute on Aging",
            "Pew Charitable Trusts",
            "U.S. National Science Foundation",
            "United States Department of Defense",
            "United States Department of Energy",
            "W. M. Keck Foundation",
            "Warren Alpert Foundation",
        }
        other_organizations = {
            "Antibodies Inc",
            "Rockland Immunochemicals",
            "Synaptic Systems",
        }
        expected_organizations = expected_funders | other_organizations

        self.assertTrue(expected_organizations.issubset(Organization.name_map))

        funder_types = get_args(Organization.FUNDERS.__origin__)
        for name in expected_funders:
            organization = Organization.from_name(name)
            self.assertTrue(any(isinstance(organization, kind) for kind in funder_types), name)


if __name__ == "__main__":
    unittest.main()
