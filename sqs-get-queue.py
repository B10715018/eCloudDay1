import boto3
import json

REGION_NAME = 'us-west-2'
client = boto3.client('sqs', region_name=REGION_NAME)

try:
    with open('./data/sqs-list-queue.json', 'r') as openfile:
        json_object = json.load(openfile)

    for item in json_object['QueueUrls']:
        try:
            response = client.get_queue_attributes(
                QueueUrl=item)
            print(response)
            with open('./data/sqs-get-queue-'+item+'.json', 'w') as outfile:
                outfile.write(json.dumps(response))
                outfile.close()
        except:
            print('Queue URL not found')
except:
    print('File not found')
