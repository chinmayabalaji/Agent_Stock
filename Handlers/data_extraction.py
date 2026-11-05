import json
import boto3
import logging
import urllib3
from datetime import datetime, timedelta

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client('s3')
requests = urllib3.PoolManager()

def get_filename():
    try:
        date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        year, month, day = date.split('-')
        file_name = f"{year}/{month}/{day}/data_{date}.json"
        return date, file_name
    except Exception as e:
        logger.error(f"Error in get_filename: {str(e)}")
        raise

def get_data(date):
    try:
        url = f"https://api.tejhq.dev/v1/snapshot/nse?date={date}&format=json"
        response = requests.request("GET", url, timeout=60)
        data = response.json()
        return data
    except Exception as e:
        logger.error(f"Error in get_data: {str(e)}")
        raise

def write_data(data, file_name):
    try:
        bucket_name = 'agent-stock-bucket'
        
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json.dumps(data))
        logger.info(f"Data written to S3: {file_name}")
    except Exception as e:
        logger.error(f"Error writing data to S3: {str(e)}")
        raise

def lambda_handler(event, context):
    try:
        date, filename = get_filename()
        data = get_data(date)
        write_data(data, filename)

    except Exception as e:
        logger.error(f"Error in lambda_handler: {str(e)}")
        raise e
