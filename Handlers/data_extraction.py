import json
import boto3
import logging
import urllib3
from datetime import datetime, timedelta

logger = logging.getLogger()
logger.basicConfig(level=logging.INFO)

s3 = boto3.client('s3')
requests = urllib3.PoolManager()

def get_date():
    try:
        date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        return date
    except Exception as e:
        logger.error(f"Error in get_date: {str(e)}")
        raise e

def get_data(date):
    try:
        url = f"https://api.example.com/data?date={date}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            raise Exception(f"Failed to fetch data: {response.status_code}")
    except Exception as e:
        logger.error(f"Error in get_data: {str(e)}")
        raise e

def write_data(data, date):
    try:
        bucket_name = 'agent-stock-bucket'
        file_name = f"{date.strftime('%Y')}/{date.strftime('%m')}/{date.strftime('%d')}/data_{date}.json"
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json.dumps(data))
        logger.info(f"Data written to S3: {file_name}")
    except Exception as e:
        logger.error(f"Error writing data to S3: {str(e)}")
        raise e

def lambda_handler(event, context):
    try:
        date = get_date()
        data = get_data(date)
        write_data(data, date)

    except Exception as e:
        logger.error(f"Error in lambda_handler: {str(e)}")
        raise e
