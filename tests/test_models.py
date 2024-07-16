"""Tests classes with fixed Literal values match defaults"""

import unittest

from aind_data_schema_models.harp_types import HarpDeviceTypes
from aind_data_schema_models.organizations import Organizations
from aind_data_schema_models.platforms import Platforms
from aind_data_schema_models.registry import Registries
from aind_data_schema_models.species import Species


class LiteralAndDefaultTests(unittest.TestCase):
    """Tests Literals match defaults in several classes"""

    def test_organizations(self):
        """Test Literals match defaults"""

        for organization in Organizations._ALL:
            model = organization()
            round_trip = model.model_validate_json(model.model_dump_json())
            self.assertIsNotNone(round_trip)

    def test_harp(self):
        """Test Literals match defaults"""

        for harp in HarpDeviceTypes._ALL:
            model = harp()
            round_trip = model.model_validate_json(model.model_dump_json())
            self.assertIsNotNone(round_trip)

    def test_registry(self):
        """Test Literals match defaults"""

        for registry in Registries._ALL:
            model = registry()
            round_trip = model.model_validate_json(model.model_dump_json())
            self.assertIsNotNone(round_trip)

    def test_platforms(self):
        """Test Literals match defaults"""

        for platform in Platforms._ALL:
            model = platform()
            round_trip = model.model_validate_json(model.model_dump_json())
            self.assertIsNotNone(round_trip)

    def test_species(self):
        """Test Literals match defaults"""

        for species in Species._ALL:
            model = species()
            round_trip = model.model_validate_json(model.model_dump_json())
            self.assertIsNotNone(round_trip)


if __name__ == "__main__":
    unittest.main()
