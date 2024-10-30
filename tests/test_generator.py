import unittest
from unittest.mock import patch, mock_open, MagicMock
from pathlib import Path
import pandas as pd
from aind_data_schema_models._generators.generator import generate_code


class TestGenerateCode(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="template content")
    @patch("pandas.read_csv")
    @patch("subprocess.run")
    @patch("jinja2.Environment.from_string")
    def test_generate_code(self, mock_from_string, mock_subprocess_run, mock_read_csv, mock_open):
        # Mock the CSV data to be used
        mock_data = pd.DataFrame({"column": ["value"]})
        mock_read_csv.return_value = mock_data

        # Mock Jinja2 template rendering
        mock_template = MagicMock()
        mock_template.render.return_value = "rendered code"
        mock_from_string.return_value = mock_template

        # Define the paths that will be used in the function
        data_type = "test_data"
        output_path = Path("./src/aind_data_schema_models/test_data.py")

        # Run the function with isort and black enabled
        generate_code(data_type, isort=True, black=True)

        # Check if the CSV file was read correctly
        mock_read_csv.assert_called_once_with(Path(f"./src/aind_data_schema_models/models/{data_type}.csv"))

        # Check if the template was read correctly
        mock_open.assert_any_call(Path(f"./src/aind_data_schema_models/_generators/templates/{data_type}.txt"))

        # Ensure the template rendering was called with the correct context
        mock_template.render.assert_called_once_with(data=mock_data)

        # Check if the output file was written with the rendered code
        mock_open().write.assert_called_once_with("rendered code")

        # Ensure isort and black were called
        mock_subprocess_run.assert_any_call(["isort", str(output_path)])
        mock_subprocess_run.assert_any_call(["black", str(output_path)])

    @patch("subprocess.run")
    @patch("jinja2.Environment.from_string")
    @patch("pandas.read_csv")
    @patch("builtins.open", new_callable=mock_open, read_data="template content")
    def test_generate_code_without_isort_black(self, mock_open, mock_read_csv, mock_from_string, mock_subprocess_run):
        # Mock the CSV data
        mock_read_csv.return_value = pd.DataFrame({"column": ["value"]})

        # Mock Jinja2 template rendering
        mock_template = MagicMock()
        mock_template.render.return_value = "rendered code"
        mock_from_string.return_value = mock_template

        # Run the function without isort and black
        generate_code("test_data", isort=False, black=False)

        # Ensure that neither isort nor black was called
        mock_subprocess_run.assert_not_called()

    @patch("pandas.read_csv", side_effect=FileNotFoundError)
    def test_generate_code_missing_data_file(self, mock_read_csv):
        # Run the function expecting a FileNotFoundError due to missing CSV file
        with self.assertRaises(FileNotFoundError):
            generate_code("missing_data")

    @patch("builtins.open", side_effect=FileNotFoundError)
    @patch("pandas.read_csv")
    def test_generate_code_missing_template_file(self, mock_read_csv, mock_open):
        # Mock the CSV data to be used
        mock_read_csv.return_value = pd.DataFrame({"column": ["value"]})

        # Run the function expecting a FileNotFoundError due to missing template file
        with self.assertRaises(FileNotFoundError):
            generate_code("missing_template")


if __name__ == "__main__":
    unittest.main()