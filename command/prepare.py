import json
import os

REGION_NAME = 'us-west-2'
ACCOUNT_ID = '758325631830'

cytoscape_data = []

''' Prepare all the lambda'''
with open('./data/lambda-list-functions.json', 'r') as openfile:
    lambda_object = json.load(openfile)
    for item in lambda_object['Functions']:
        cytoscape_data.append({
            "data": {
                "type": "lambda",
                "id": item["FunctionArn"],
                "region": 'us-west-2',
                "name": item['FunctionName'],
            }
        })

    openfile.close()

''' Prepare all the dynamodb tables'''
with open('./data/dynamodb-list-table.json', 'r') as openfile:
    ddb_object = json.load(openfile)
    for item in ddb_object['TableNames']:
        cytoscape_data.append({
            "data": {
                "type": "dynamodb",
                "id": 'ddb:'+item,
                "region": "us-west-2",
                "name": item,
            }
        })
    openfile.close()

'''Prepare for transcribe'''
list_of_files = os.listdir('./data')  # list of files in the data directory
for each_file in list_of_files:
    # since its all type str you can simply use startswith
    if each_file.startswith('cloudtrail-start-transcription'):
        print('Found a cloudtrail transcribe file')
        cytoscape_data.append({
            "data": {
                "type": "transcribe",
                "id": "transcribe",
                "region": "us-west-2",
                "name": "transcribe",
            }
        })
        break

'''Prepare for translate'''
list_of_files = os.listdir('./data')  # list of files in the data directory
for each_file in list_of_files:
    # since its all type str you can simply use startswith
    if each_file.startswith('cloudtrail-translate-text-'):
        print('Found a cloudtrail translate file')
        cytoscape_data.append({
            "data": {
                "type": "translate",
                "id": "translate",
                "region": "us-west-2",
                "name": "translate",
            }
        })
        break

'''FIND CONNECTION BETWEEN DDB AND LAMBDA'''
for item in lambda_object['Functions']:
    for ddb in ddb_object['TableNames']:
        try:
            if item['Environment']['Variables']['DB_TABLE_NAME'] == ddb:
                # print('Found connection between {} and {}'.format(
                #     item['FunctionName'], ddb))
                cytoscape_data.append({
                    "data": {
                        "id": item['FunctionName'] + '-ddb:' + ddb,
                        "source": item["FunctionArn"],
                        "target": 'ddb:'+ddb,
                    }
                })
        except:
            print('No connection between {} and {}'.format(
                item['FunctionName'], ddb))

'''FIND CONNECTION BETWEEN LAMBDA AND TRANSCRIBE'''
list_of_files = os.listdir('./data')  # list of files in the data directory
for each_file in list_of_files:
    # since its all type str you can simply use startswith
    if each_file.startswith('cloudtrail-start-transcription'):
        with open('./data/' + each_file, 'r') as openfile:
            cloudtrail_transcribe_object = json.load(openfile)
            try:
                if 'AWS_Lambda' in cloudtrail_transcribe_object['userAgent']:
                    lambda_arn = 'arn:aws:lambda:'+REGION_NAME+':'+ACCOUNT_ID + \
                        ':function:' + \
                        (cloudtrail_transcribe_object['userIdentity']
                         ['principalId'].split(':')[-1])
                    transcribe_edge_data = {
                        "data": {
                            "id": lambda_arn+'-'+'transcribe',
                            "source": lambda_arn,
                            "target": 'transcribe',
                        }
                    }
                    if(cytoscape_data.count(transcribe_edge_data) == 0):
                        cytoscape_data.append(transcribe_edge_data)
                    print('Found connection between transcribe and lambda:{}'.format(
                        cloudtrail_transcribe_object['userIdentity']['principalId'].split(':')[-1]))
            except:
                print('No connection between lambda and transcribe')
        openfile.close()

'''FIND CONNECTION BETWEEN TRANSCRIBE AND S3'''

'''FIND CONNECTION BETWEEN LAMBDA AND TRANSLATE'''
list_of_files = os.listdir('./data')  # list of files in the data directory
for each_file in list_of_files:
    # since its all type str you can simply use startswith
    if each_file.startswith('cloudtrail-translate-text-'):
        with open('./data/' + each_file, 'r') as openfile:
            cloudtrail_translate_object = json.load(openfile)
            try:
                if 'AWS_Lambda' in cloudtrail_translate_object['userAgent']:
                    lambda_arn = 'arn:aws:lambda:'+REGION_NAME+':'+ACCOUNT_ID + \
                        ':function:' + \
                        (cloudtrail_translate_object['userIdentity']
                         ['principalId'].split(':')[-1])
                    translate_edge_data = {
                        "data": {
                            "id": lambda_arn+'-'+'translate',
                            "source": lambda_arn,
                            "target": 'translate',
                        }
                    }
                    if(cytoscape_data.count(translate_edge_data) == 0):
                        cytoscape_data.append(translate_edge_data)
                    print('Found connection between translate and lambda:{}'.format(
                        cloudtrail_translate_object['userIdentity']['principalId'].split(':')[-1]))
            except:
                print('No connection between lambda and translate')
        openfile.close()

with open('./data/data.json', 'w') as outfile:
    outfile.write(json.dumps(cytoscape_data))
    outfile.close()
