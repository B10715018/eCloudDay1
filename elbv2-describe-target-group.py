import boto3
import json
client=boto3.client('elbv2',region_name='us-west-2')
response = client.describe_target_groups(
    LoadBalancerArn='arn:aws:elasticloadbalancing:us-west-2:758325631830:loadbalancer/app/appELB/5982e05975655deb',
)
print(response)
json_list=json.dumps(response)
with open('./data/elbv2-describe-target-group'+'.json','w')as outfile:
        outfile.write(json_list)
        outfile.close()
