import boto3
import json
import os

REGION_NAME = 'us-west-2'


def sqs_list_queue():
    client = boto3.client('sqs', region_name=REGION_NAME)

    response = client.list_queues(
    )

    json_list = json.dumps(response)
    script_dir = os.path.dirname('.')
    file_path = os.path.join(script_dir, 'data/sqs-list-queue.json')
    with open(file_path, 'w')as outfile:
        outfile.write(json_list)
        outfile.close()
