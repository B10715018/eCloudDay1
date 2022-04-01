import boto3
import json

REGION_NAME = 'us-west-2'
client = boto3.client('sqs', region_name=REGION_NAME)

try:
    with open('./data/sqs-list-queue.json', 'r') as openfile:
        json_object = json.load(openfile)

    count = 0
    for item in json_object['QueueUrls']:
        response = client.get_queue_attributes(
            QueueUrl=item)
        with open('./data/sqs-get-queue-'+str(count)+'.json', 'w') as outfile:
            outfile.write(json.dumps(response))
            count += 1
            outfile.close()
except:
    print('File not found for sqs-get-queue')
