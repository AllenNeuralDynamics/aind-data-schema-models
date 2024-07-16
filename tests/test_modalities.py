"""Tests classes in modalities module"""

import unittest

from aind_data_schema_models.modalities import Modalities


class TestModality(unittest.TestCase):
    """Tests methods in Modality class"""

    def test_from_abbreviation(self):
        """Tests modality can be constructed from abbreviation"""

        self.assertEqual(Modalities.Ecephys, Modality.from_abbreviation("ecephys"))


if __name__ == "__main__":
    unittest.main()
