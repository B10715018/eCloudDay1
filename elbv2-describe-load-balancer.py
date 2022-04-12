import boto3
import json
REGION_NAME = 'us-west-2'
client = boto3.client('elbv2', region_name=REGION_NAME)
response = client.describe_load_balancers()
dateList = []
count = 0
for item in response['LoadBalancers']:
    count += 1
    dateList.append(json.dumps(item['CreatedTime'], default=str))

for i in range(count):
    response['LoadBalancers'][i]['CreatedTime'] = dateList[i]

json_list = json.dumps(response)
with open('./data/elbv2-describe-load-balancer'+'.json', 'w')as outfile:
    outfile.write(json_list)
    outfile.close()
