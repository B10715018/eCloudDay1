import boto3
import json
import os

REGION_NAME = 'us-west-2'


def sqs_get_queue():
    client = boto3.client('sqs', region_name=REGION_NAME)
    script_dir = os.path.dirname('.')
    file_path_read = os.path.join(script_dir, 'data/sqs-list-queue.json')
    try:
        with open(file_path_read, 'r') as openfile:
            json_object = json.load(openfile)

        count = 0
        for item in json_object['QueueUrls']:
            response = client.get_queue_attributes(
                QueueUrl=item)
            file_path_write = os.path.join(
                script_dir, 'data/sqs-get-queue-'+str(count)+'.json')
            with open(file_path_write, 'w') as outfile:
                outfile.write(json.dumps(response))
                count += 1
                outfile.close()
    except:
        print('File not found for sqs-get-queue')
