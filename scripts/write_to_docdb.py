"""Module to publish models to docdb"""

import os
import csv
from typing import Iterator
from aind_data_access_api.document_db import Client as DocDBClient

DOCDB_HOST = os.getenv("DOCDB_HOST")
DOCDB_DATABASE = os.getenv("DOCDB_DATABASE")

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
            # Get all items from each csv file/model type, e.g. all modalities
            csv_file_path = os.path.join(folder_path, file_name)
            json_models = csv_to_json(csv_file_path)
            # Each model type is written to its own collection
            collection_name = file_name[:-4]
            with DocDBClient(
                host=DOCDB_HOST,
                database=DOCDB_DATABASE,
                collection=collection_name,
            ) as docdb_client:
                # Process each item in the csv
                # Assumes each item has a unique "name" field
                for json_model in json_models:
                    # Delete existing records with the same name
                    name = json_model["name"]
                    filter = {"name": json_model["name"]}
                    records = docdb_client.retrieve_docdb_records(
                        filter_query=filter,
                        projection={"_id": 1},
                    )
                    if records:
                        print(f"Deleting {len(records)} existing records for {collection_name}, name={name}")
                        ids_to_delete = [r["_id"] for r in records]
                        response = docdb_client.delete_many_records(data_asset_record_ids=ids_to_delete)
                        print(response.json())

                    # Insert new record
                    print(f"Inserting new record for {collection_name}, name={name}")
                    response = docdb_client.insert_one_docdb_record(record=json_model)
                    print(response.json())


if __name__ == "__main__":
    folder_path = PATH_TO_MODELS
    publish_to_docdb(folder_path=folder_path)