import boto3
import json
import os


def elbv2_describe_target_health(region,AWS_ACCESS_KEY,AWS_SECRET_KEY):
    client = boto3.client('elbv2', region_name=region,
    aws_access_key_id=AWS_ACCESS_KEY,aws_secret_access_key=AWS_SECRET_KEY)
    try:
        # list of files in the data directory
        list_of_files = os.listdir('./data/elbv2-target-group')
        for each_file in list_of_files:
            # since its all type str you can simply use startswith
            if each_file.startswith('elbv2-describe-target-group-'):
                script_dir = os.path.dirname(
                    './data/elbv2-target-group/')
                file_path_read=os.path.join(script_dir,each_file)
                f = open(file_path_read, 'r')
                data = json.load(f)
                count = 0
                TargetGroupArnList = []
                for item in data['TargetGroups']:
                    count += 1
                    TargetGroupArnList.append(item['TargetGroupArn'])
                    for i in range(count):
                        response = client.describe_target_health(
                            TargetGroupArn=TargetGroupArnList[i]
                        )
                        json_list = json.dumps(response)
                        script_dir_2=os.path.dirname('.')
                        file_path_write = os.path.join(
                            script_dir_2, 'data/elbv2-target-health/elbv2-describe-target-health-'+item['TargetGroupName']+'-'+region+'.json')
                        with open(file_path_write, 'w')as outfile:
                            outfile.write(json_list)
                            outfile.close()
    except:
        print('Error in describe target health')
