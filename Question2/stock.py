import datetime
import json
import random
import boto3

STREAM_NAME = "input-stream"
REGION = "us-north-1"

def get_data():
    return {
        'event_time': datetime.datetime.now().isoformat(),
        'ticker': random.choice(["AC","KH","ALL", "IL"]),
        'price': round(random.random() * 100, 2)}

def generate(stream_name, kinesis_client):
    while True:
        data = get_data()
        print(data)
       #kinesis_client.put_record(StreamName=stream_name,Data=json.dumps(data),PartitionKey="partitionkey")

if __name__ == '__main__':
    generate(STREAM_NAME, boto3.client('kinesis', region_name=REGION))