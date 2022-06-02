import boto3
import json
import os


def resource_group_list_group_resources(region, AWS_ACCESS_KEY, AWS_SECRET_KEY):
    client = boto3.client('resource-groups', region_name=region,
                          aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
    try:
        script_dir = os.path.dirname('.')
        file_path_read = os.path.join(
            script_dir, 'data/resource-group-list-groups-'+region+'.json')
        f = open(file_path_read, 'r')
        data = json.load(f)
        groupARN = []
        groupName = []
        count = 0
        for item in data['GroupIdentifiers']:
            groupARN.append(item['GroupArn'])
            groupName.append(item['GroupName'])
            count += 1
        for i in range(count):
            try:
                response = client.list_group_resources(
                    Group=groupARN[i]
                )
                json_response = json.dumps(response)
                file_path_write = os.path.join(
                    script_dir, 'data/resource-group-resources/resource-group-list-group-resources-'+region+'-'+groupName[i]+'.json')
                with open(file_path_write, 'w') as outfile:
                    outfile.write(json_response)
                    outfile.close()
            except:
                print('Error in get group resources')

    except:
        print('File not found for list group resources')
