import boto3
import json
import os


def elb_list_tags(region, AWS_ACCESS_KEY, AWS_SECRET_KEY):
    client = boto3.client('elbv2', region_name=region,
                          aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
    ElbArnList = []
    ElbNameList = []
    count = 0
    script_dir = os.path.dirname('.')
    file_path = os.path.join(
        script_dir, 'data/elbv2-describe-load-balancer-'+region+'.json')
    f = open(file_path, 'r')
    data = json.load(f)

    for item in data['LoadBalancers']:
        ElbArnList.append(item['LoadBalancerArn'])
        ElbNameList.append(item['LoadBalancerName'])
        count += 1
    for i in range(count):
        # get tags for each elb
        response = client.describe_tags(
            ResourceArns=[ElbArnList[i], ]
        )
        json_list = json.dumps(response["TagDescriptions"], indent=4)
        file_path2 = os.path.join(
            script_dir, 'data/elbv2-list-tags/elbv2-list-tags-' +
            ElbNameList[i]+"-"
            + region+'.json')
        with open(file_path2, 'w')as outfile:
            outfile.write(json_list)
            outfile.close()
