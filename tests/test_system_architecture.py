import unittest
from aind_data_schema_models.system_architecture import OperatingSystem, CPUArchitecture


class UnitsTests(unittest.TestCase):
    """Class for testing Utils.Units"""

    def test_units(self):
        """Tests creation of a SizeVal object"""

        self.assertIsNotNone(OperatingSystem.MACOS_SONOMA)
        self.assertIsNotNone(CPUArchitecture.X86_64)
