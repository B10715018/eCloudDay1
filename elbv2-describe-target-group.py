import boto3
import json
REGION_NAME='us-west-2'
client = boto3.client('elbv2', region_name=REGION_NAME)
try:

    f = open('./data/elbv2-describe-load-balancer.json')
    data = json.load(f)
    count = 0
    LoadBalancerArnList = []
    for item in data['LoadBalancers']:
        count += 1
        LoadBalancerArnList.append(item['LoadBalancerArn'])
    for i in range(count):
        try:
            response = client.describe_target_groups(
            LoadBalancerArn=LoadBalancerArnList[i],
            )
            json_list = json.dumps(response)
            print(json_list)
            with open('./data/elbv2-describe-target-group'+LoadBalancerArnList[i]+'.json', 'w')as outfile:
                outfile.write(json_list)
                outfile.close()

        except:
            print('Error in describe target group')
except:
    print('File not found for elbv2-describe-target-group')