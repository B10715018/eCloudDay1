import boto3
import json
import os


def elbv2_describe_target_group(region,AWS_ACCESS_KEY,AWS_SECRET_KEY):
    try:
        client = boto3.client('elbv2', region_name=region,
        aws_access_key_id=AWS_ACCESS_KEY,aws_secret_access_key=AWS_SECRET_KEY)
        script_dir = os.path.dirname('.')
        file_path_read = os.path.join(
            script_dir, 'data/elbv2-describe-load-balancer-'+region+'.json')
        f = open(file_path_read, 'r')
        data = json.load(f)
        for item in data['LoadBalancers']:
            response = client.describe_target_groups(
                LoadBalancerArn=item['LoadBalancerArn'],
            )
            json_list = json.dumps(response)
            file_path_write = os.path.join(
                script_dir, 'data/elbv2-target-group/elbv2-describe-target-group-'+item['LoadBalancerName']+'-'+region+'.json')
            with open(file_path_write, 'w')as outfile:
                outfile.write(json_list)
                outfile.close()
            
    except:
        print('Error in describe target group')
