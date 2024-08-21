import os
import csv
from typing import Iterator
from aind_data_access_api.document_db_ssh import (
    DocumentDbSSHClient,
    DocumentDbSSHCredentials,
)

DB_NAME = os.getenv("DB_NAME")
DOCDB_READWRITE_SECRET = os.getenv("READWRITE_SECRET")
DOCDB_SSH_TUNNEL_SECRET = os.getenv("DOCDB_SSH_TUNNEL_SECRET")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")


def csv_to_json(csv_file_path: str) -> Iterator:
    """
    Returns Iterator of dict
    """
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            yield row


def publish_to_docdb(folder_path: str, credentials: DocumentDbSSHCredentials) -> None:
    """
    Writes models to docdb
    """
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):
            collection = file_name[:-4]
            credentials.collection = collection
            csv_file_path = os.path.join(folder_path, file_name)
            json_data = csv_to_json(csv_file_path)
            with DocumentDbSSHClient(credentials=credentials) as doc_db_client:
                for records in json_data:
                    filter = {"name": records["name"]}
                    response = doc_db_client.collection.update_one(filter=filter, update={"$set": records}, upsert=True)
                    print(response.raw_result)


if __name__ == "__main__":
    folder_path = '../models'
    credentials = DocumentDbSSHCredentials.from_secrets_manager(
        doc_db_secret_name=DOCDB_READWRITE_SECRET,
        ssh_secret_name=DOCDB_SSH_TUNNEL_SECRET
    )
    credentials.database = DB_NAME
    publish_to_docdb(folder_path, credentials)
