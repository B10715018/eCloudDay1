from ast import Return
import boto3
import json

REGION_NAME = 'us-west-2'

client = boto3.client('sns', region_name=REGION_NAME)

# open file for searching all kind of sns topic
try:
    with open('./data/sns-list-topic-'+REGION_NAME+'.json', 'r')as openfile:
        json_object = json.load(openfile)

    snsArnList = []
    # get all the sns topic in specified region
    for item in json_object['Topics']:
        # get the topic attribute for each sns and write into json file
        try:
            response = client.get_topic_attributes(
                TopicArn=item['TopicArn'])
            json_list = json.dumps(response)
            with open('./data/sns-get-topic-attribute-'+item['TopicArn']+'.json', 'w') as outfile:
                outfile.write(json_list)
                outfile.close()
        except:
            print('Something is Error')

except:
    print('File not found for sns-get-topic-attr')
