import boto3
import json
import datetime

client=boto3.client('ec2',region_name='us-west-2')
response = client.describe_network_interfaces()
def defaultconverter(o):
  if isinstance(o, datetime.datetime):
      return o.__str__()
json_list=json.dumps(response,default = defaultconverter)
with open('./data/ec2-describe-network-interface.json','w') as outfile:
  outfile.write(json_list)
  outfile.close()
