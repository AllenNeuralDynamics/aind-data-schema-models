"""Module to publish models to docdb"""

import csv
import os
from typing import Iterator
from uuid import uuid4

from aind_data_access_api.document_db import Client as DocDBClient
from requests import HTTPError

DOCDB_HOST = os.getenv("DOCDB_HOST")
DOCDB_DATABASE = os.getenv("DOCDB_DATABASE")
DOCDB_COLLECTION = os.getenv("DOCDB_COLLECTION")

PATH_TO_MODELS = os.getenv("PATH_TO_MODELS")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")


def csv_to_json(csv_file_path: str) -> Iterator:
    """
    Returns Iterator of dict
    """
    with open(csv_file_path, mode="r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            yield row


def publish_to_docdb(folder_path: str) -> None:
    """
    Writes models to docdb
    """
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".csv"):
            print(f"Processing file: {file_name}")
            # Get all items from each csv file, e.g. all modalities
            csv_file_path = os.path.join(folder_path, file_name)
            csv_contents = list(csv_to_json(csv_file_path))
            # Create 1 record that contains all items
            # Assumes file size does not exceed API gateway and DocDB limits
            record = {
                "_id": file_name.removesuffix(".csv"),
                "file_name": file_name,
                "count": len(csv_contents),
                "contents": csv_contents,
            }
            # Upsert to docdb
            with DocDBClient(
                host=DOCDB_HOST,
                database=DOCDB_DATABASE,
                collection=DOCDB_COLLECTION,
            ) as docdb_client:
                print(f"Upserting {file_name} contents to {DOCDB_DATABASE}/{DOCDB_COLLECTION}")
                response = docdb_client.upsert_one_docdb_record(record=record)
                print(response.json())


if __name__ == "__main__":
    folder_path = PATH_TO_MODELS
    try:
        publish_to_docdb(folder_path=folder_path)
    except HTTPError as error:
        print(f"HTTP error {error.response.status_code}: {error.response.text}")
        raise error
