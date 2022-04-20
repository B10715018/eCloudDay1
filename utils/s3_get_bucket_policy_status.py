import boto3
import json
import os
REGION_NAME = 'us-west-2'


def s3_get_bucket_policy_status():
    client = boto3.client('s3', region_name=REGION_NAME)
    try:
        script_dir = os.path.dirname('.')
        file_path = os.path.join(script_dir, 'data/s3-list-bucket.json')
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
                filename = (script_dir, 'data/s3-' +
                            BucketNameList[i]+'-policy-status.json')
                with open(filename, 'w') as outfile:
                    outfile.write(json_response)
                    outfile.close()
            except:
                print('Error in getPolicyStatus')

    except:
        print('Error in get policy status')
