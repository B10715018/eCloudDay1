import json
import boto3

client=boto3.client('wafv2',region_name='us-west-2')
response = client.get_web_acl(
  Name='wafELB',
  Scope='REGIONAL',
  Id='43b16080-94e8-4dbf-9b4e-166898878bc0',
)
json_list=json.dumps(response)
print(response)
with open('./data/waf-get-web-acl'+'.json','w')as outfile:
        outfile.write(json_list)
        outfile.close()



