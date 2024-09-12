"""Testing script for system architecture classes"""

import unittest
from aind_data_schema_models.system_architecture import OperatingSystem, CPUArchitecture


class UnitsTests(unittest.TestCase):
    """Class for testing Utils.Units"""

    def test_system_architecture(self):
        """Tests that OperatingSystem/CPUArchitecture instantiate"""

        self.assertIsNotNone(OperatingSystem.MACOS_SONOMA)
        self.assertIsNotNone(CPUArchitecture.X86_64)
