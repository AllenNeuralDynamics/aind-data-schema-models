"""Test coordinate_enums"""

import unittest

from aind_data_schema_models.device_enums import BinMode


class UnitsTests(unittest.TestCase):
    """Class for testing coordinate_enums"""

    def test_units(self):
        """Tests creation of a SizeVal object"""

        self.assertIsNotNone(BinMode.ADDITIVE)


if __name__ == "__main__":
    unittest.main()
