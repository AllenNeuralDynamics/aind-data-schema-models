"""Dev utils tests"""

import unittest
import pandas as pd
from aind_data_schema_models._generators.dev_utils import unique_rows, to_class_name, to_class_name_underscored


class TestDevUtils(unittest.TestCase):
    """Tests for dev_utils module"""

    def test_unique_rows(self):
        """Test unique_rows function"""

        data = pd.DataFrame({"id": [1, 2, 2, 3, 4, 4, 5], "value": ["a", "b", "b", "c", "d", "d", "e"]})
        key = "id"
        expected_output = pd.DataFrame({"id": [1, 2, 3, 4, 5], "value": ["a", "b", "c", "d", "e"]})

        result = unique_rows(data, key).reset_index(drop=True)
        self.assertEqual(result.shape, expected_output.shape)
        self.assertEqual(result.to_dict(), expected_output.to_dict())

    def test_to_class_name(self):
        """Test to class name method"""

        # Regular cases
        self.assertEqual(to_class_name("Smart SPIM"), "Smart_Spim")
        self.assertEqual(to_class_name("SmartSPIM"), "Smartspim")
        self.assertEqual(to_class_name("single-plane-ophys"), "Single_Plane_Ophys")

        # Edge cases
        self.assertEqual(to_class_name("a-b-c"), "A_B_C")  # Hyphenated
        self.assertEqual(to_class_name("_Already-Underscored"), "_Already_Underscored")

        # Check that non-alphanumeric characters are replaced with _
        self.assertEqual(to_class_name("123test"), "_123Test")  # Replace number with _
        self.assertEqual(to_class_name("#a"), "_A")  # Replace alphanumeric with _
        self.assertEqual(to_class_name("1Smart 2Spim"), "_1Smart_2Spim")  # Replace alphanumeric with _

        # Empty string
        self.assertEqual(to_class_name(""), "")

    def test_to_class_name_underscored(self):
        """Test to class name underscored method"""

        # Regular cases
        self.assertEqual(to_class_name_underscored("Smart SPIM"), "_Smart_Spim")
        self.assertEqual(to_class_name_underscored("SmartSPIM"), "_Smartspim")
        self.assertEqual(to_class_name_underscored("single-plane-ophys"), "_Single_Plane_Ophys")

        # Edge cases
        self.assertEqual(to_class_name_underscored("123test"), "_123Test")  # Starts with a number
        self.assertEqual(to_class_name_underscored("a-b-c"), "_A_B_C")  # Hyphenated
        self.assertEqual(to_class_name_underscored("_Already-Underscored"), "__Already_Underscored")
        self.assertEqual(to_class_name_underscored("#a"), "__A")  # Strip non-alphanumeric characters
        self.assertEqual(to_class_name_underscored("1Smart 2Spim"), "_1Smart_2Spim")  # Replace alphanumeric with _

        # Empty string
        self.assertEqual(to_class_name_underscored(""), "_")  # Should still return an underscore


if __name__ == "__main__":
    unittest.main()
