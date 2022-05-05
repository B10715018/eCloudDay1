import boto3
import os
import json

def rscgroup_list_group_resource(region):
    client = boto3.client('resource-groups', region_name=region)
    try:
        script_dir = os.path.dirname('.')
        file_path = os.path.join(
            script_dir, 'data/rscgroup-list-group-'+region+'.json')
        f = open(file_path)
        data = json.load(f)
        count = 0
        GroupNameList = []
        for item in data['Groups']:
            count += 1
            GroupNameList.append(item['Name'])
        for i in range(count):
            try:
                response = client.list_group_resources(
                    GroupName=GroupNameList[i],
                )
                json_response = json.dumps(response, indent=4)
                filename = os.path.join(script_dir, 'data/rscgroup-group-resource/rscgroup-' +
                                        GroupNameList[i]+'list-group-resource-'+region+'.json')
                with open(filename, 'w') as outfile:
                    outfile.write(json_response)
                    outfile.close()
            except:
                print('Error in list group resource : no resource generate')
    except:
        print('Error in list group resource : file not found')








  


