from pathlib import Path
import unittest
from unittest.mock import patch, MagicMock
import os
from aind_data_schema_models.scripts.write_to_docdb import csv_to_json, publish_to_docdb
from aind_data_access_api.document_db_ssh import (
    DocumentDbSSHCredentials,
)

TEST_DIRECTORY = Path(os.path.dirname(os.path.realpath(__file__)))
SAMPLE_CSV_FILE = TEST_DIRECTORY / "resources" / "harp_types.csv"


class TestWriteToDocdb(unittest.TestCase):

    def test_csv_to_json(self):
        # Test that csv_to_json correctly converts CSV to a list of dicts
        expected_output = [{"name": "Behavior", "whoami": "1216"},
                           {"name": "Cuttlefish", "whoami": "1403"},
                           {"name": "Treadmill", "whoami": "1402"}]
        actual_output = list(csv_to_json(SAMPLE_CSV_FILE))
        self.assertEqual(expected_output, actual_output)

    @patch("os.listdir", return_value=["test.csv"])
    @patch("os.path.join", return_value="dummy_path/test.csv")
    @patch("aind_data_schema_models.scripts.write_to_docdb.csv_to_json",
           return_value=iter([{"name": "Alice", "age": "30"}])
           )
    @patch("aind_data_schema_models.scripts.write_to_docdb.DocumentDbSSHClient")
    def test_publish_to_docdb(self, mock_doc_db_client_cls, mock_csv_to_json, mock_os_path_join, mock_os_listdir):
        # Setup
        mock_doc_db_client = MagicMock()
        mock_doc_db_client_cls.return_value.__enter__.return_value = mock_doc_db_client

        credentials = DocumentDbSSHCredentials(
            host="doc_db_host",
            username="doc_db_username",
            password="doc_db_password",
            ssh_host="123.456.789.0",
            ssh_username="ssh_username",
            ssh_password="ssh_password",
        )
        credentials.collection = None

        # Execute
        publish_to_docdb("dummy_folder_path", credentials)

        # Assert
        mock_os_listdir.assert_called_once_with("dummy_folder_path")
        mock_os_path_join.assert_called_once_with("dummy_folder_path", "test.csv")
        mock_csv_to_json.assert_called_once_with("dummy_path/test.csv")

        mock_doc_db_client.collection.update_one.assert_called_once_with(
            filter={"name": "Alice"},
            update={"$set": {"name": "Alice", "age": "30"}},
            upsert=True
        )
        self.assertEqual(credentials.collection, "test")


if __name__ == "__main__":
    unittest.main()
