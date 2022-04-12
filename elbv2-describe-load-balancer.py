import boto3
import json
REGION_NAME = 'us-west-2'
client = boto3.client('elbv2', region_name=REGION_NAME)
try:
    f = open('./data/elbv2-describe-load-balancer.json')
    data = json.load(f)
    count = 0
    TargetGroupArnList = []
    for item in data['TargetGroups']:
        count += 1
        TargetGroupArnList.append(item['TargetGroupArn'])
        print(TargetGroupArnList)
    try:
        for i in range(count):
            response = client.describe_target_health(
                TargetGroupArn=TargetGroupArnList[i]
            )
        json_list = json.dumps(response)
        with open('./data/elbv2-describe-target-health'+TargetGroupArnList[i]+'.json', 'w')as outfile:
            outfile.write(json_list)
            outfile.close()
    except:
        print('Error in elbv2-describe-target-health')
except:
    print('File not found for elbv2-describe-target-health')
