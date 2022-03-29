import boto3
import json
client=boto3.client('elbv2',region_name='us-west-2')
response = client.describe_load_balancers(
)

dateList=[]
count=0
for item in response['LoadBalancers']:
  count+=1
  dateList.append(json.dumps(items))
with open('./data/elbv2-describe-load-balancer'+'.json','w')as outfile:
        outfile.write(json_list)
        outfile.close()
print(response)