import boto3
import json

client = boto3.client('s3', region_name='us-west-2')
try:
    f = open('./data/s3-list-bucket.json')
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
            filename = './data/s3-'+BucketNameList[i]+'-policy.json'
            with open(filename, 'w') as outfile:
                outfile.write(json_response)
                outfile.close()
        except:
            print('Error in getPolicy')

except:
    print('File not found for s3-get-bucket-policy')
