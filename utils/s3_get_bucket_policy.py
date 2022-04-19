import boto3
import json
import os

REGION_NAME = 'us-west-2'
client = boto3.client('s3', region_name=REGION_NAME)

def s3_get_bucket_policy():
    try:

        script_dir = os.path.dirname('.')
        file_path = os.path.join(script_dir, 'data/s3-list-bucket.json')
        f = open(file_path, 'r')
        data = json.load(f)
        count = 0
        BucketNameList = []

        for item in data['Buckets']:
            count += 1
            BucketNameList.append(item['Name'])
            # print(BucketNameList)

        for i in range(count):
            try:
                response = client.get_bucket_policy(
                    Bucket=BucketNameList[i]
                )
                json_response = json.dumps(response)
                file_path2 = os.path.join(
                script_dir, 'data/lambda-'+BucketNameList[i]+'-policy.json')
                with open(file_path2, 'w') as outfile:
                    outfile.write(json_response)
                    outfile.close()

            except:
                print('Error in getPolicy')

    except:
        print('File not found for s3-get-bucket-policy')
