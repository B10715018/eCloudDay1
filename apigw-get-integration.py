import boto3
from json import JSONEncoder
import datetime
import json

# subclass JSONEncoder

class DateTimeEncoder(JSONEncoder):
    # Override the default method
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()


client = boto3.client('apigateway', region_name='us-west-2')
response = client.get_integration(
    restApiId='zk0oea00u9',
    resourceId='k6lwvk7le7',
    httpMethod='GET'
)

json_list = json.dumps(response, indent=4, cls=DateTimeEncoder)
with open('./data/apigw-get-integration'+'.json', 'w')as outfile:
    outfile.write(json_list)
    outfile.close()