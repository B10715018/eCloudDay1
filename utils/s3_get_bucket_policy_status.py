import boto3
import json
import os


def s3_get_bucket_policy_status(region):
    client = boto3.client('s3', region_name=region)
    try:
        script_dir = os.path.dirname('.')
        file_path = os.path.join(
            script_dir, 'data/s3-list-bucket-'+region+'.json')
        f = open(file_path)
        data = json.load(f)
        count = 0
        BucketNameList = []
        for item in data['Buckets']:
            count += 1
            BucketNameList.append(item['Name'])

        for i in range(count):
            try:
                response = client.get_bucket_policy_status(
                    Bucket=BucketNameList[i],
                )
                json_response = json.dumps(response)
                filename = (script_dir, 'data/s3-policy-status/s3-' +
                            BucketNameList[i]+'-policy-status-'+region+'.json')
                with open(filename, 'w') as outfile:
                    outfile.write(json_response)
                    outfile.close()
            except:
                print('Error in getPolicyStatus')

    except:
        print('Error in get policy status')
