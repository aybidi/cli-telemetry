import os
import yaml
from datetime import datetime

import click
from google.cloud import bigquery

def _get_secrets():
    with open("secrets/gcp-secrets.yaml", "r") as file:
        secrets = yaml.safe_load(file)
    return secrets

def upload_data(data):
    client = bigquery.Client()
    secrets = _get_secrets()
    project_id, dataset_id, table_id = secrets["PROJECT_ID"], secrets["BQ_DATASET_ID"], secrets["TABLE_ID"]

    # schema = [
    #     bigquery.SchemaField("time", "STRING", mode="REQUIRED"),
    #     bigquery.SchemaField("user", "STRING", mode="REQUIRED"),
    #     bigquery.SchemaField("command", "STRING", mode="REQUIRED"),
    # ]

    # table = bigquery.Table(f"{project_id}.{dataset_id}.{table_id}", schema=schema)
    # table = client.create_table(table)

    data_to_send = [
        {
            "time": "2022-11-07",
            "user": os.getenv("USER", "unspecified"),
            "command": data
        }
    ]
    errors = client.insert_rows_json(
        f"{project_id}.{dataset_id}.{table_id}", data_to_send
    )

    if errors:
        click.secho("encountered error while uploading to BQ", fg="red")
