import boto3
import json
client = boto3.client('elbv2', region_name='us-west-2')
response = client.describe_target_health(
    TargetGroupArn='arn:aws:elasticloadbalancing:us-west-2:758325631830:targetgroup/MyELBTG/a8647a6fccb86b88',
)

json_list = json.dumps(response)
with open('./data/elbv2-describe-target-health'+'.json', 'w')as outfile:
    outfile.write(json_list)
    outfile.close()
