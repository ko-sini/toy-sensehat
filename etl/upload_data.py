"""Functions to upload sensehat data to AWS s3."""

import logging
import os
from configparser import ConfigParser
from datetime import datetime

import boto3
import pandas as pd
from botocore.exceptions import ClientError
from sense_hat import SenseHat

config = ConfigParser()
with open("./etl/.cfg", encoding="utf-8") as cfg:
    config.read_file(cfg)

def s3_object_exists(
    resource,
    bucket_name: str,
    object_name: str,
):
    try:
        resource.Object(bucket_name, object_name).load()
    except ClientError as err:
        if err.response['Error']['Code'] == "404":
            return False  # object does not exist
        logging.error(err)
        raise ClientError from err # something else went wrong
    return True  # object exists

def upload_to_s3(
    client,
    bucket_name: str,
    object_name: str,
    file_name: str,
):
    try:
        client.upload_file(file_name, bucket_name, object_name)
    except ClientError as err:
        logging.error(err)
        return False
    return True

def get_sensehat_data():
    sense = SenseHat()
    dt = datetime.now()
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()
    return pd.DataFrame(
        data=[[dt.date(), dt.time(), temperature, humidity, pressure]],
        columns=["date", "time", "temperature", "humidity", "pressure"]
    )

def upload_sensehat_data(
    temp_path: str = "./temp/temp.h5",
):
    resource = boto3.resource("s3")
    client = boto3.client("s3")

    # Create temporary directory if one doesn't exist
    if not os.path.exists(os.path.dirname(temp_path)):
        os.mkdir(os.path.dirname(temp_path))

    # Create/append new data
    data = get_sensehat_data()
    if s3_object_exists(resource, config["etl"]["bucket_name"], config["etl"]["object_name"]):
        # TODO: error handling for download_file
        client.download_file(config["etl"]["bucket_name"], config["etl"]["object_name"], temp_path)
        existing_data = pd.read_hdf(temp_path)
        data = pd.concat([data, existing_data])

    # Display and store temporary data
    print(data)
    data.to_hdf(temp_path, key="data")

    # Upload to s3
    upload_to_s3(client, config["etl"]["bucket_name"], config["etl"]["object_name"], temp_path)

    # Remove temporary data
    os.remove(temp_path)


if __name__ == "__main__":
    upload_sensehat_data()
