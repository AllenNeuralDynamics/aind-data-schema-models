"""Dev utils tests"""

import unittest
import pandas as pd
from aind_data_schema_models._generators.dev_utils import unique_rows


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


if __name__ == "__main__":
    unittest.main()
