import boto3
import json
REGION_NAME = 'us-west-2'


def elbv2_describe_target_group():
    client = boto3.client('elbv2', region_name=REGION_NAME)
    try:
        script_dir = os.path.dirname('.')
        file_path = os.path.join(
            script_dir, 'data/elbv2-describe-load-balancer.json')
        f = open(file_path, 'r')
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
                # print(json_list)
                file_path2 = os.path.join(
                    script_dir, 'data/elbv2-describe-target-group'+LoadBalancerArnList[i]+'.json')
                with open(file_path2, 'w')as outfile:
                    outfile.write(json_list)
                    outfile.close()

            except:
                print('Error in describe target group')
    except:
        print('File not found for elbv2-describe-target-group')
