"""Test device_enums"""

import unittest

from aind_data_schema_models.device_enums import BinMode


class UnitsTests(unittest.TestCase):
    """Class for testing device_enums"""

    def test_units(self):
        """Tests creation of a BinMode object"""

        self.assertIsNotNone(BinMode.ADDITIVE)


if __name__ == "__main__":
    unittest.main()
