import boto3
from json import JSONEncoder
import datetime
import json
import os
# subclass JSONEncoder
REGION_NAME = 'us-west-2'


def apigw_get_integration():
    class DateTimeEncoder(JSONEncoder):
        # Override the default method
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()

    script_dir = os.path.dirname('.')
    file_path = os.path.join(script_dir, 'data/apigw-get-rest-apis.json')
    f = open(file_path, 'r')
    data = json.load(f)
    count = 0
    count2 = 0
    count3 = 0
    RestApiIdList = []
    ResourceIdList = []
    MethodList = []
    for item in data['items']:
        count += 1
        RestApiIdList.append(item['id'])

    for i in range(count):
        file_path2 = os.path.join(
            script_dir, 'data/apigw-get-resources-'+RestApiIdList[i]+'.json')
        a = open(file_path2, 'r')
        resource = json.load(a)

        for Id in resource['items']:
            ResourceIdList.append(Id['id'])
            count2 += 1
        try:
            for j in range(count2):
                new_ResourceId = ResourceIdList[j]
                count3 += 1
                MethodList.append(Id['resourceMethods'])
                new_menthod = list(MethodList[0].keys())
            try:
                for k in range(count3):
                    client = boto3.client(
                        'apigateway', region_name=REGION_NAME)
                    response = client.get_integration(
                        restApiId=RestApiIdList[i],
                        resourceId=ResourceIdList[j],
                        httpMethod=new_menthod[k]
                    )

                    json_list = json.dumps(
                        response, indent=4, cls=DateTimeEncoder)
                    file_path3 = os.path.join(
                        script_dir, 'data/apigw-get-integration-'+RestApiIdList[i]+'.json')
                    with open(file_path3, 'w')as outfile:
                        outfile.write(json_list)
                        outfile.close()
            except:
                print('intergration not found')
        except:
            print('methond not found')
