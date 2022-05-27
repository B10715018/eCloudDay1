import os
import json


def export_to_JSON(cytoscape_node_data, cytoscape_edge_data):
    filtered_cytoscape_data = []
    cytoscape_miscellaneous_data=[{
        "tag":{
            "Application": [],
            "Department": [],
            "Environment": [],
            "Project": [],
            "Owner": [],
            "Other": []
        },
        "region": []
    }]
    # filtered the node data into one new array consisting tag and region
    for tag in cytoscape_node_data['tag']:
        for tag_keys in tag:
            if(tag_keys=='Application'):
                print('Application')
            elif(tag_keys=='Application'):
                print('Department')
    filtered_cytoscape_data.append(cytoscape_node_data)
    filtered_cytoscape_data.append(cytoscape_edge_data)
    script_dir = os.path.dirname('.')
    file_path_write = os.path.join(
        script_dir, 'data/data.json')
    with open(file_path_write, 'w') as outfile:
        outfile.write(json.dumps(filtered_cytoscape_data))
        outfile.close()

export_to_JSON([
        {
            "data": {
                "type": "Lambda",
                "id": "arn:aws:lambda:us-west-2:758325631830:function:ReadS3FileAndCheckStatus",
                "arn": "arn:aws:lambda:us-west-2:758325631830:function:ReadS3FileAndCheckStatus",
                "runtime": "python3.9",
                "timeout": 3,
                "memory_size": 128,
                "version": "$LATEST",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "ReadS3FileAndCheckStatus",
                "description": "",
                "role": "arn:aws:iam::758325631830:role/CloudDay1ReaderRole",
                "codesize": 855,
                "tag": {
                    "Application": "Processing",
                    "Department": "Intership",
                    "Environment": "Pre-Prod",
                    "Owner": "Back-end",
                    "Project": "Architecture"
                },
                "cost_for_month": "0.03 USD"
            }
        },
        {
            "data": {
                "type": "Lambda",
                "id": "arn:aws:lambda:us-west-2:758325631830:function:Test_withSNS",
                "arn": "arn:aws:lambda:us-west-2:758325631830:function:Test_withSNS",
                "runtime": "python3.7",
                "timeout": 3,
                "memory_size": 128,
                "version": "$LATEST",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "Test_withSNS",
                "description": "",
                "role": "arn:aws:iam::758325631830:role/CloudDay1ReaderRole",
                "codesize": 1127,
                "tag": {},
                "cost_for_month": "0.03 USD"
            }
        },
        {
            "data": {
                "type": "Lambda",
                "id": "arn:aws:lambda:us-west-2:758325631830:function:ListUserInformation",
                "arn": "arn:aws:lambda:us-west-2:758325631830:function:ListUserInformation",
                "runtime": "python3.9",
                "timeout": 3,
                "memory_size": 128,
                "version": "$LATEST",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "ListUserInformation",
                "description": "",
                "role": "arn:aws:iam::758325631830:role/ListUserInformationRole",
                "codesize": 809,
                "tag": {
                    "Application": "Processing",
                    "Department": "Intership",
                    "Environment": "Pre-Prod",
                    "Owner": "Back-end",
                    "Project": "Architecture"
                },
                "cost_for_month": "0.03 USD"
            }
        },
        {
            "data": {
                "type": "Lambda",
                "id": "arn:aws:lambda:us-west-2:758325631830:function:auto-turnoff-a665cf10-99f5-11ec-8fc5-0a7e1f31bb99",
                "arn": "arn:aws:lambda:us-west-2:758325631830:function:auto-turnoff-a665cf10-99f5-11ec-8fc5-0a7e1f31bb99",
                "runtime": "python3.8",
                "timeout": 10,
                "memory_size": 128,
                "version": "$LATEST",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "auto-turnoff-a665cf10-99f5-11ec-8fc5-0a7e1f31bb99",
                "description": "",
                "role": "arn:aws:iam::758325631830:role/instance-num-checker-role-a665cf10-99f5-11ec-8fc5-0a7e1f31bb99",
                "codesize": 557,
                "tag": {
                    "aws:cloudformation:logical-id": "AutoTurnOffFunction",
                    "aws:cloudformation:stack-id": "arn:aws:cloudformation:us-west-2:758325631830:stack/auto-turn-off/a665cf10-99f5-11ec-8fc5-0a7e1f31bb99",
                    "aws:cloudformation:stack-name": "auto-turn-off"
                },
                "cost_for_month": "0.03 USD"
            }
        },
        {
            "data": {
                "type": "Lambda",
                "id": "arn:aws:lambda:us-west-2:758325631830:function:stepFunction_getText",
                "arn": "arn:aws:lambda:us-west-2:758325631830:function:stepFunction_getText",
                "runtime": "python3.7",
                "timeout": 300,
                "memory_size": 128,
                "version": "$LATEST",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "stepFunction_getText",
                "description": "",
                "role": "arn:aws:iam::758325631830:role/CloudDay1ReaderRole",
                "codesize": 929,
                "tag": {
                    "Application": "Processing",
                    "Department": "Intership",
                    "Environment": "Prod",
                    "Owner": "Back-end",
                    "Project": "Clouday1",
                    "stepfunction": "translate"
                },
                "cost_for_month": "0.03 USD",
                "parent": "arn:aws:states:us-west-2:758325631830:stateMachine:lambda"
            }
        },
        {
            "data": {
                "type": "Lambda",
                "id": "arn:aws:lambda:us-west-2:758325631830:function:stepFunction_createNewRequest",
                "arn": "arn:aws:lambda:us-west-2:758325631830:function:stepFunction_createNewRequest",
                "runtime": "python3.7",
                "timeout": 3,
                "memory_size": 128,
                "version": "$LATEST",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "stepFunction_createNewRequest",
                "description": "",
                "role": "arn:aws:iam::758325631830:role/CloudDay1ReaderRole",
                "codesize": 593,
                "tag": {
                    "Application": "Processing",
                    "Department": "Intership",
                    "Environment": "Prod",
                    "Owner": "Back-end",
                    "Project": "Clouday1",
                    "stepfunction": "stepFunction_ConvertToText"
                },
                "cost_for_month": "0.03 USD",
                "parent": "arn:aws:states:us-west-2:758325631830:stateMachine:lambda"
            }
        },
        {
            "data": {
                "type": "Lambda",
                "id": "arn:aws:lambda:us-west-2:758325631830:function:DeleteUserData",
                "arn": "arn:aws:lambda:us-west-2:758325631830:function:DeleteUserData",
                "runtime": "python3.9",
                "timeout": 3,
                "memory_size": 128,
                "version": "$LATEST",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "DeleteUserData",
                "description": "",
                "role": "arn:aws:iam::758325631830:role/dynamo_all_role",
                "codesize": 708,
                "tag": {},
                "cost_for_month": "0.03 USD"
            }
        },
        {
            "data": {
                "type": "Lambda",
                "id": "arn:aws:lambda:us-west-2:758325631830:function:CloudDayOne_NewRequest",
                "arn": "arn:aws:lambda:us-west-2:758325631830:function:CloudDayOne_NewRequest",
                "runtime": "python3.7",
                "timeout": 3,
                "memory_size": 128,
                "version": "$LATEST",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "CloudDayOne_NewRequest",
                "description": "",
                "role": "arn:aws:iam::758325631830:role/CloudDay1ReaderRole",
                "codesize": 637,
                "tag": {
                    "UseSns": ""
                },
                "cost_for_month": "0.03 USD",
                "parent": "arn:aws:states:us-west-2:758325631830:stateMachine:SnS"
            }
        },
        {
            "data": {
                "type": "Lambda",
                "id": "arn:aws:lambda:us-west-2:758325631830:function:CloudDayOne_GetRequestedText",
                "arn": "arn:aws:lambda:us-west-2:758325631830:function:CloudDayOne_GetRequestedText",
                "runtime": "python3.7",
                "timeout": 300,
                "memory_size": 128,
                "version": "$LATEST",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "CloudDayOne_GetRequestedText",
                "description": "",
                "role": "arn:aws:iam::758325631830:role/CloudDay1ReaderRole",
                "codesize": 542,
                "tag": {
                    "UseSns": ""
                },
                "cost_for_month": "0.03 USD"
            }
        },
        {
            "data": {
                "type": "Lambda",
                "id": "arn:aws:lambda:us-west-2:758325631830:function:CloudDay1_GetText",
                "arn": "arn:aws:lambda:us-west-2:758325631830:function:CloudDay1_GetText",
                "runtime": "python3.7",
                "timeout": 300,
                "memory_size": 128,
                "version": "$LATEST",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "CloudDay1_GetText",
                "description": "",
                "role": "arn:aws:iam::758325631830:role/CloudDay1ReaderRole",
                "codesize": 951,
                "tag": {
                    "UseSns": ""
                },
                "cost_for_month": "0.03 USD",
                "parent": "arn:aws:states:us-west-2:758325631830:stateMachine:SnS"
            }
        },
        {
            "data": {
                "type": "Lambda",
                "id": "arn:aws:lambda:us-west-2:758325631830:function:ReadS3JsonFile",
                "arn": "arn:aws:lambda:us-west-2:758325631830:function:ReadS3JsonFile",
                "runtime": "python3.7",
                "timeout": 3,
                "memory_size": 128,
                "version": "$LATEST",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "ReadS3JsonFile",
                "description": "",
                "role": "arn:aws:iam::758325631830:role/service-role/ReadS3JsonFile-role-wlb1b0u1",
                "codesize": 395,
                "tag": {},
                "cost_for_month": "0.03 USD"
            }
        },
        {
            "data": {
                "type": "Lambda",
                "id": "arn:aws:lambda:us-west-2:758325631830:function:stepFunction_triggerStepFunction",
                "arn": "arn:aws:lambda:us-west-2:758325631830:function:stepFunction_triggerStepFunction",
                "runtime": "python3.7",
                "timeout": 60,
                "memory_size": 128,
                "version": "$LATEST",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "stepFunction_triggerStepFunction",
                "description": "",
                "role": "arn:aws:iam::758325631830:role/CloudDay1ReaderRole",
                "codesize": 508,
                "tag": {
                    "Application": "Processing",
                    "Department": "Intership",
                    "Environment": "Prod",
                    "Owner": "Back-end",
                    "Project": "Clouday1",
                    "triggerstepfuncation": "stepfunction"
                },
                "cost_for_month": "0.03 USD"
            }
        },
        {
            "data": {
                "type": "Lambda",
                "id": "arn:aws:lambda:us-west-2:758325631830:function:aesd-CleanupBucketFunction-AuZH4vSPUKLb",
                "arn": "arn:aws:lambda:us-west-2:758325631830:function:aesd-CleanupBucketFunction-AuZH4vSPUKLb",
                "runtime": "python3.8",
                "timeout": 900,
                "memory_size": 128,
                "version": "$LATEST",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "aesd-CleanupBucketFunction-AuZH4vSPUKLb",
                "description": "Custom Lambda resource for emptying S3 buckets on stack deletion",
                "role": "arn:aws:iam::758325631830:role/aesd-CleanupBucketFunctionRole-LJBUXCKYBIOA",
                "codesize": 8765717,
                "tag": {
                    "aws:cloudformation:logical-id": "CleanupBucketFunction",
                    "aws:cloudformation:stack-id": "arn:aws:cloudformation:us-west-2:758325631830:stack/aesd/0978dd20-ca90-11ec-8e6f-06f0b04d699d",
                    "aws:cloudformation:stack-name": "aesd",
                    "lambda:createdBy": "SAM"
                },
                "cost_for_month": "0.03 USD"
            }
        },
        {
            "data": {
                "type": "Lambda",
                "id": "arn:aws:lambda:us-west-2:758325631830:function:listAllRequest",
                "arn": "arn:aws:lambda:us-west-2:758325631830:function:listAllRequest",
                "runtime": "python3.7",
                "timeout": 3,
                "memory_size": 128,
                "version": "$LATEST",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "listAllRequest",
                "description": "",
                "role": "arn:aws:iam::758325631830:role/dynamo_all_role",
                "codesize": 516,
                "tag": {},
                "cost_for_month": "0.03 USD"
            }
        },
        {
            "data": {
                "type": "Lambda",
                "id": "arn:aws:lambda:us-west-2:758325631830:function:stepFunction_ConvertToText",
                "arn": "arn:aws:lambda:us-west-2:758325631830:function:stepFunction_ConvertToText",
                "runtime": "python3.7",
                "timeout": 300,
                "memory_size": 128,
                "version": "$LATEST",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "stepFunction_ConvertToText",
                "description": "",
                "role": "arn:aws:iam::758325631830:role/CloudDay1ReaderRole",
                "codesize": 1081,
                "tag": {
                    "Application": "Processing",
                    "Department": "Intership",
                    "Environment": "Prod",
                    "Owner": "Back-end",
                    "Project": "Clouday1",
                    "stepfunction": "stepFunction_GetRequestedText"
                },
                "cost_for_month": "0.03 USD",
                "parent": "arn:aws:states:us-west-2:758325631830:stateMachine:lambda"
            }
        },
        {
            "data": {
                "type": "Lambda",
                "id": "arn:aws:lambda:us-west-2:758325631830:function:PostUser",
                "arn": "arn:aws:lambda:us-west-2:758325631830:function:PostUser",
                "runtime": "python3.9",
                "timeout": 3,
                "memory_size": 128,
                "version": "$LATEST",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "PostUser",
                "description": "",
                "role": "arn:aws:iam::758325631830:role/dynamo_all_role",
                "codesize": 480,
                "tag": {},
                "cost_for_month": "0.03 USD"
            }
        },
        {
            "data": {
                "type": "Lambda",
                "id": "arn:aws:lambda:us-west-2:758325631830:function:stepFunction_GetRequestedText",
                "arn": "arn:aws:lambda:us-west-2:758325631830:function:stepFunction_GetRequestedText",
                "runtime": "python3.7",
                "timeout": 3,
                "memory_size": 128,
                "version": "$LATEST",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "stepFunction_GetRequestedText",
                "description": "",
                "role": "arn:aws:iam::758325631830:role/CloudDay1ReaderRole",
                "codesize": 543,
                "tag": {
                    "api": "getResquestToWeb",
                    "clouday1": ""
                },
                "cost_for_month": "0.03 USD"
            }
        },
        {
            "data": {
                "type": "Lambda",
                "id": "arn:aws:lambda:us-west-2:758325631830:function:CloudDay1_ConvertToText",
                "arn": "arn:aws:lambda:us-west-2:758325631830:function:CloudDay1_ConvertToText",
                "runtime": "python3.7",
                "timeout": 300,
                "memory_size": 128,
                "version": "$LATEST",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "CloudDay1_ConvertToText",
                "description": "",
                "role": "arn:aws:iam::758325631830:role/CloudDay1ReaderRole",
                "codesize": 1127,
                "tag": {
                    "UseSns": ""
                },
                "cost_for_month": "0.03 USD",
                "parent": "arn:aws:states:us-west-2:758325631830:stateMachine:SnS"
            }
        },
        {
            "data": {
                "type": "S3",
                "id": "arn:aws:s3:::aesd-costandusageathenaresultsbucket-13ojvos05qktv",
                "arn": "arn:aws:s3:::aesd-costandusageathenaresultsbucket-13ojvos05qktv",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "aesd-costandusageathenaresultsbucket-13ojvos05qktv",
                "CreationDate": "2022-05-03T03:22:06+00:00",
                "tag": {
                    "aws:cloudformation:stack-id": "arn:aws:cloudformation:us-west-2:758325631830:stack/aesd/0978dd20-ca90-11ec-8e6f-06f0b04d699d",
                    "aws:cloudformation:stack-name": "aesd",
                    "aws:cloudformation:logical-id": "CostAndUsageAthenaResultsBucket"
                },
                "cost_for_month": "0.26 USD"
            }
        },
        {
            "data": {
                "type": "S3",
                "id": "arn:aws:s3:::aesd-costandusagereportbucket-1beseo5o1z13x",
                "arn": "arn:aws:s3:::aesd-costandusagereportbucket-1beseo5o1z13x",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "aesd-costandusagereportbucket-1beseo5o1z13x",
                "CreationDate": "2022-05-03T03:22:04+00:00",
                "tag": {
                    "aws:cloudformation:stack-id": "arn:aws:cloudformation:us-west-2:758325631830:stack/aesd/0978dd20-ca90-11ec-8e6f-06f0b04d699d",
                    "aws:cloudformation:stack-name": "aesd",
                    "aws:cloudformation:logical-id": "CostAndUsageReportBucket"
                },
                "cost_for_month": "0.26 USD"
            }
        },
        {
            "data": {
                "type": "S3",
                "id": "arn:aws:s3:::aesd-discoverybucket-1g6tduazcd53u",
                "arn": "arn:aws:s3:::aesd-discoverybucket-1g6tduazcd53u",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "aesd-discoverybucket-1g6tduazcd53u",
                "CreationDate": "2022-05-03T03:22:05+00:00",
                "tag": {
                    "aws:cloudformation:stack-id": "arn:aws:cloudformation:us-west-2:758325631830:stack/aesd/0978dd20-ca90-11ec-8e6f-06f0b04d699d",
                    "aws:cloudformation:stack-name": "aesd",
                    "aws:cloudformation:logical-id": "DiscoveryBucket"
                },
                "cost_for_month": "0.26 USD"
            }
        },
        {
            "data": {
                "type": "S3",
                "id": "arn:aws:s3:::aesd-webuibucket-45igum9wtbzl",
                "arn": "arn:aws:s3:::aesd-webuibucket-45igum9wtbzl",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "aesd-webuibucket-45igum9wtbzl",
                "CreationDate": "2022-05-03T03:21:41+00:00",
                "tag": {
                    "aws:cloudformation:stack-id": "arn:aws:cloudformation:us-west-2:758325631830:stack/aesd/0978dd20-ca90-11ec-8e6f-06f0b04d699d",
                    "aws:cloudformation:stack-name": "aesd",
                    "aws:cloudformation:logical-id": "WebUIBucket"
                },
                "cost_for_month": "0.26 USD"
            }
        },
        {
            "data": {
                "type": "S3",
                "id": "arn:aws:s3:::audio-json",
                "arn": "arn:aws:s3:::audio-json",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "audio-json",
                "CreationDate": "2022-05-12T14:45:03+00:00",
                "tag": {
                    "Project": "Clouday1",
                    "Environment": "Pre-Prod",
                    "Department": "Intership",
                    "Owner": "DBA",
                    "Application": "database"
                },
                "cost_for_month": "0.26 USD"
            }
        },
        {
            "data": {
                "type": "S3",
                "id": "arn:aws:s3:::aws-clouday1-cloud9-bucket",
                "arn": "arn:aws:s3:::aws-clouday1-cloud9-bucket",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "aws-clouday1-cloud9-bucket",
                "CreationDate": "2022-03-09T05:18:26+00:00",
                "tag": {},
                "cost_for_month": "0.26 USD"
            }
        },
        {
            "data": {
                "type": "S3",
                "id": "arn:aws:s3:::aws-cloudtrail-logs-758325631830-22d3da20",
                "arn": "arn:aws:s3:::aws-cloudtrail-logs-758325631830-22d3da20",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "aws-cloudtrail-logs-758325631830-22d3da20",
                "CreationDate": "2022-04-07T10:09:09+00:00",
                "tag": {},
                "cost_for_month": "0.26 USD"
            }
        },
        {
            "data": {
                "type": "S3",
                "id": "arn:aws:s3:::aws-cloudtrail-logs-758325631830-8a3cc63f",
                "arn": "arn:aws:s3:::aws-cloudtrail-logs-758325631830-8a3cc63f",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "aws-cloudtrail-logs-758325631830-8a3cc63f",
                "CreationDate": "2022-03-24T08:25:47+00:00",
                "tag": {},
                "cost_for_month": "0.26 USD"
            }
        },
        {
            "data": {
                "type": "S3",
                "id": "arn:aws:s3:::aws-cloudtrail-logs-758325631830-9c97109b",
                "arn": "arn:aws:s3:::aws-cloudtrail-logs-758325631830-9c97109b",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "aws-cloudtrail-logs-758325631830-9c97109b",
                "CreationDate": "2022-03-31T09:40:55+00:00",
                "tag": {},
                "cost_for_month": "0.26 USD"
            }
        },
        {
            "data": {
                "type": "S3",
                "id": "arn:aws:s3:::aws-cloudtrail-logs-758325631830-a8a59988",
                "arn": "arn:aws:s3:::aws-cloudtrail-logs-758325631830-a8a59988",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "aws-cloudtrail-logs-758325631830-a8a59988",
                "CreationDate": "2022-03-23T09:58:55+00:00",
                "tag": {},
                "cost_for_month": "0.26 USD"
            }
        },
        {
            "data": {
                "type": "S3",
                "id": "arn:aws:s3:::aws-cloudtrail-logs-758325631830-ade2f357",
                "arn": "arn:aws:s3:::aws-cloudtrail-logs-758325631830-ade2f357",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "aws-cloudtrail-logs-758325631830-ade2f357",
                "CreationDate": "2022-03-31T09:51:53+00:00",
                "tag": {},
                "cost_for_month": "0.26 USD"
            }
        },
        {
            "data": {
                "type": "S3",
                "id": "arn:aws:s3:::aws-cloudtrail-logs-758325631830-b4e41710",
                "arn": "arn:aws:s3:::aws-cloudtrail-logs-758325631830-b4e41710",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "aws-cloudtrail-logs-758325631830-b4e41710",
                "CreationDate": "2022-03-21T01:50:47+00:00",
                "tag": {},
                "cost_for_month": "0.26 USD"
            }
        },
        {
            "data": {
                "type": "S3",
                "id": "arn:aws:s3:::aws-cloudtrail-logs-758325631830-cognito",
                "arn": "arn:aws:s3:::aws-cloudtrail-logs-758325631830-cognito",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "aws-cloudtrail-logs-758325631830-cognito",
                "CreationDate": "2022-04-20T02:32:56+00:00",
                "tag": {},
                "cost_for_month": "0.26 USD"
            }
        },
        {
            "data": {
                "type": "S3",
                "id": "arn:aws:s3:::aws-cloudtrail-logs-758325631830-de70d49b",
                "arn": "arn:aws:s3:::aws-cloudtrail-logs-758325631830-de70d49b",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "aws-cloudtrail-logs-758325631830-de70d49b",
                "CreationDate": "2022-03-21T01:10:33+00:00",
                "tag": {},
                "cost_for_month": "0.26 USD"
            }
        },
        {
            "data": {
                "type": "S3",
                "id": "arn:aws:s3:::aws-cloudtrail-logs-758325631830-e4deb78d",
                "arn": "arn:aws:s3:::aws-cloudtrail-logs-758325631830-e4deb78d",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "aws-cloudtrail-logs-758325631830-e4deb78d",
                "CreationDate": "2022-03-21T02:36:58+00:00",
                "tag": {},
                "cost_for_month": "0.26 USD"
            }
        },
        {
            "data": {
                "type": "S3",
                "id": "arn:aws:s3:::aws-cloudtrail-logs-congito",
                "arn": "arn:aws:s3:::aws-cloudtrail-logs-congito",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "aws-cloudtrail-logs-congito",
                "CreationDate": "2022-04-20T02:30:51+00:00",
                "tag": {},
                "cost_for_month": "0.26 USD"
            }
        },
        {
            "data": {
                "type": "S3",
                "id": "arn:aws:s3:::aws-sam-cli-managed-default-samclisourcebucket-147ovz4e57qyo",
                "arn": "arn:aws:s3:::aws-sam-cli-managed-default-samclisourcebucket-147ovz4e57qyo",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "aws-sam-cli-managed-default-samclisourcebucket-147ovz4e57qyo",
                "CreationDate": "2022-04-02T04:35:01+00:00",
                "tag": {
                    "aws:cloudformation:stack-name": "aws-sam-cli-managed-default",
                    "aws:cloudformation:logical-id": "SamCliSourceBucket",
                    "ManagedStackSource": "AwsSamCli",
                    "aws:cloudformation:stack-id": "arn:aws:cloudformation:eu-west-2:758325631830:stack/aws-sam-cli-managed-default/26cb31d0-b23e-11ec-a483-02edf7e9d1c6"
                },
                "cost_for_month": "0.26 USD"
            }
        },
        {
            "data": {
                "type": "S3",
                "id": "arn:aws:s3:::cf-templates-pqf8ay94fwmy-us-west-2",
                "arn": "arn:aws:s3:::cf-templates-pqf8ay94fwmy-us-west-2",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "cf-templates-pqf8ay94fwmy-us-west-2",
                "CreationDate": "2022-03-14T02:29:44+00:00",
                "tag": {},
                "cost_for_month": "0.26 USD"
            }
        },
        {
            "data": {
                "type": "S3",
                "id": "arn:aws:s3:::clouday1-metadata",
                "arn": "arn:aws:s3:::clouday1-metadata",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "clouday1-metadata",
                "CreationDate": "2022-05-12T14:44:30+00:00",
                "tag": {
                    "Project": "Architecture",
                    "Environment": "Pre-Prod",
                    "Department": "Intership",
                    "Owner": "DBA",
                    "Application": "database"
                },
                "cost_for_month": "0.26 USD"
            }
        },
        {
            "data": {
                "type": "S3",
                "id": "arn:aws:s3:::clouday1-userdata",
                "arn": "arn:aws:s3:::clouday1-userdata",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "clouday1-userdata",
                "CreationDate": "2022-05-12T14:48:08+00:00",
                "tag": {
                    "Project": "Architecture",
                    "Environment": "Pre-Prod",
                    "Department": "Intership",
                    "Owner": "DBA",
                    "Application": "Database"
                },
                "cost_for_month": "0.26 USD"
            }
        },
        {
            "data": {
                "type": "S3",
                "id": "arn:aws:s3:::clouday1architecture",
                "arn": "arn:aws:s3:::clouday1architecture",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "clouday1architecture",
                "CreationDate": "2022-05-12T14:50:01+00:00",
                "tag": {
                    "Project": "Architecture",
                    "Environment": "Pre-Prod",
                    "Department": "Intership",
                    "Owner": "Front-end",
                    "Application": "web"
                },
                "cost_for_month": "0.26 USD"
            }
        },
        {
            "data": {
                "type": "S3",
                "id": "arn:aws:s3:::config-bucket-758325631830",
                "arn": "arn:aws:s3:::config-bucket-758325631830",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "config-bucket-758325631830",
                "CreationDate": "2022-03-23T06:44:41+00:00",
                "tag": {},
                "cost_for_month": "0.26 USD"
            }
        },
        {
            "data": {
                "type": "S3",
                "id": "arn:aws:s3:::testsdsdsd",
                "arn": "arn:aws:s3:::testsdsdsd",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "testsdsdsd",
                "CreationDate": "2022-03-01T03:10:24+00:00",
                "tag": {},
                "cost_for_month": "0.26 USD"
            }
        },
        {
            "data": {
                "type": "S3",
                "id": "arn:aws:s3:::testv2-s3bq30m-1216tkkzvctfw",
                "arn": "arn:aws:s3:::testv2-s3bq30m-1216tkkzvctfw",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "testv2-s3bq30m-1216tkkzvctfw",
                "CreationDate": "2022-03-17T09:48:14+00:00",
                "tag": {
                    "aws:cloudformation:stack-id": "arn:aws:cloudformation:us-west-2:758325631830:stack/testv2/59825c70-a5d7-11ec-acb0-022e96007245",
                    "aws:cloudformation:stack-name": "testv2",
                    "aws:cloudformation:logical-id": "S3BQ30M"
                },
                "cost_for_month": "0.26 USD"
            }
        },
        {
            "data": {
                "type": "S3",
                "id": "arn:aws:s3:::translate-website",
                "arn": "arn:aws:s3:::translate-website",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "translate-website",
                "CreationDate": "2022-05-12T14:51:54+00:00",
                "tag": {
                    "Project": "Clouday1",
                    "Department": "Intership",
                    "Owner": "Front-end",
                    "congnito": "identity pool",
                    "Environment": "Pre-Prod",
                    "clouday1": "",
                    "api": "stepFunction_triggerStepFunction",
                    "Application": "web",
                    "UseSns": ""
                },
                "cost_for_month": "0.26 USD"
            }
        },
        {
            "data": {
                "type": "S3",
                "id": "arn:aws:s3:::upload-video-translate",
                "arn": "arn:aws:s3:::upload-video-translate",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "upload-video-translate",
                "CreationDate": "2022-03-01T04:24:07+00:00",
                "tag": {},
                "cost_for_month": "0.26 USD"
            }
        },
        {
            "data": {
                "type": "DynamoDB",
                "id": "arn:aws:dynamodb:us-west-2:758325631830:table/architectureDB",
                "region": "us-west-2",
                "name": "architectureDB",
                "account_id": "758325631830",
                "itemCount": 8,
                "partition_key": "requestID",
                "items": [
                    "account_name",
                    "data_name",
                    "user_id",
                    "status",
                    "timestamp",
                    "region",
                    "account_id",
                    "requestID"
                ],
                "tag": {
                    "Project": "Architecture",
                    "Department": "Intership",
                    "Owner": "DBA",
                    "Environment": "Pre-Prod",
                    "Application": "database"
                },
                "cost_for_month": "17.03 USD"
            }
        },
        {
            "data": {
                "type": "DynamoDB",
                "id": "arn:aws:dynamodb:us-west-2:758325631830:table/translate",
                "region": "us-west-2",
                "name": "translate",
                "account_id": "758325631830",
                "itemCount": 91,
                "partition_key": "ID",
                "items": [
                    "status",
                    "translatedText",
                    "mediaFormat",
                    "text",
                    "ID",
                    "url",
                    "language"
                ],
                "tag": {
                    "Project": "Clouday1",
                    "Department": "Intership",
                    "Owner": "DBA",
                    "getRequest": "stepFunction_GetRequestedText",
                    "Environment": "Pre-Prod",
                    "Application": "database"
                },
                "cost_for_month": "17.03 USD"
            }
        },
        {
            "data": {
                "type": "Transcribe",
                "id": "transcribe",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "transcribe",
                "cost_for_month": "24.04 USD"
            }
        },
        {
            "data": {
                "type": "Translate",
                "id": "translate",
                "region": "us-west-2",
                "account_id": "758325631830",
                "name": "translate",
                "cost_for_month": "15.00 USD"
            }
        },
        {
            "data": {
                "type": "SNS",
                "id": "arn:aws:sns:us-west-2:758325631830:aws-cloudtrail-logs-758325631830-b8da47bb",
                "arn": "arn:aws:sns:us-west-2:758325631830:aws-cloudtrail-logs-758325631830-b8da47bb",
                "account_id": "758325631830",
                "region": "us-west-2",
                "name": "aws-cloudtrail-logs-758325631830-b8da47bb",
                "tag": {},
                "cost_for_month": "1.50 USD"
            }
        },
        {
            "data": {
                "type": "SNS",
                "id": "arn:aws:sns:us-west-2:758325631830:getTranslatedText",
                "arn": "arn:aws:sns:us-west-2:758325631830:getTranslatedText",
                "account_id": "758325631830",
                "region": "us-west-2",
                "name": "getTranslatedText",
                "tag": {
                    "Project": "Clouday1",
                    "Environment": "Prod",
                    "Department": "Intership",
                    "Owner": "Back-end",
                    "Application": "processing",
                    "UseSns": ""
                },
                "cost_for_month": "1.50 USD",
                "parent": "arn:aws:states:us-west-2:758325631830:stateMachine:SnS"
            }
        },
        {
            "data": {
                "type": "SNS",
                "id": "arn:aws:sns:us-west-2:758325631830:newAudio",
                "arn": "arn:aws:sns:us-west-2:758325631830:newAudio",
                "account_id": "758325631830",
                "region": "us-west-2",
                "name": "newAudio",
                "tag": {
                    "Project": "Clouday1",
                    "Environment": "Prod",
                    "Department": "Intership",
                    "Owner": "Back-end",
                    "Application": "processing",
                    "UseSns": ""
                },
                "cost_for_month": "1.50 USD",
                "parent": "arn:aws:states:us-west-2:758325631830:stateMachine:SnS"
            }
        },
        {
            "data": {
                "type": "Step-Functions",
                "id": "arn:aws:states:us-west-2:758325631830:stateMachine:SnS",
                "arn": "arn:aws:states:us-west-2:758325631830:stateMachine:SnS",
                "account_id": "758325631830",
                "region": "us-west-2",
                "name": "SnS",
                "CreationDate": "\"2022-03-23 15:45:04.793000+08:00\"",
                "tag": {},
                "cost_for_month": "0.65 USD"
            }
        },
        {
            "data": {
                "type": "Step-Functions",
                "id": "arn:aws:states:us-west-2:758325631830:stateMachine:lambda",
                "arn": "arn:aws:states:us-west-2:758325631830:stateMachine:lambda",
                "account_id": "758325631830",
                "region": "us-west-2",
                "name": "lambda",
                "CreationDate": "\"2022-03-02 14:52:28.769000+08:00\"",
                "tag": {
                    "Project": "Clouday1",
                    "Department": "Intership",
                    "Owner": "Back-end",
                    "stepfunction": "translate",
                    "Environment": "Prod",
                    "clouday1": "",
                    "Application": "processing"
                },
                "cost_for_month": "0.65 USD"
            }
        },
        {
            "data": {
                "id": "arn:aws:execute-api:us-west-2:758325631830:417d1mz313",
                "arn": "arn:aws:execute-api:us-west-2:758325631830:417d1mz313",
                "type": "API Gateway",
                "name": "PerspectiveWebRestAPI",
                "account_id": "758325631830",
                "region": "us-west-2",
                "resource": [
                    {
                        "id": "5zz1n4",
                        "parentId": "aw9gt7aim9",
                        "pathPart": "resources",
                        "path": "/resources",
                        "resourceMethods": {
                            "OPTIONS": {}
                        }
                    },
                    {
                        "id": "aw9gt7aim9",
                        "path": "/"
                    }
                ],
                "tag": {
                    "aws:cloudformation:logical-id": "PerspectiveWebRestAPI",
                    "aws:cloudformation:stack-id": "arn:aws:cloudformation:us-west-2:758325631830:stack/aesd/0978dd20-ca90-11ec-8e6f-06f0b04d699d",
                    "aws:cloudformation:stack-name": "aesd"
                },
                "cost_for_month": "3.50 USD"
            }
        },
        {
            "data": {
                "id": "arn:aws:execute-api:us-west-2:758325631830:4u76mvjhub",
                "arn": "arn:aws:execute-api:us-west-2:758325631830:4u76mvjhub",
                "type": "API Gateway",
                "name": "PerspectiveServerAPI",
                "account_id": "758325631830",
                "region": "us-west-2",
                "resource": [
                    {
                        "id": "ddt5ci7w61",
                        "path": "/"
                    },
                    {
                        "id": "ffd8sl",
                        "parentId": "ddt5ci7w61",
                        "pathPart": "search",
                        "path": "/search"
                    },
                    {
                        "id": "rgfwu9",
                        "parentId": "ddt5ci7w61",
                        "pathPart": "resources",
                        "path": "/resources"
                    }
                ],
                "tag": {
                    "aws:cloudformation:logical-id": "ServerGremlinAPI",
                    "aws:cloudformation:stack-id": "arn:aws:cloudformation:us-west-2:758325631830:stack/aesd/0978dd20-ca90-11ec-8e6f-06f0b04d699d",
                    "aws:cloudformation:stack-name": "aesd"
                },
                "cost_for_month": "3.50 USD"
            }
        },
        {
            "data": {
                "id": "arn:aws:execute-api:us-west-2:758325631830:5qz90oi4mc",
                "arn": "arn:aws:execute-api:us-west-2:758325631830:5qz90oi4mc",
                "type": "API Gateway",
                "name": "PerspectiveDrawioWebRestAPI",
                "account_id": "758325631830",
                "region": "us-west-2",
                "resource": [
                    {
                        "id": "rvawrx45c1",
                        "path": "/"
                    },
                    {
                        "id": "y5uhjr",
                        "parentId": "rvawrx45c1",
                        "pathPart": "resources",
                        "path": "/resources",
                        "resourceMethods": {
                            "OPTIONS": {}
                        }
                    }
                ],
                "tag": {
                    "aws:cloudformation:logical-id": "PerspectiveDrawioWebRestAPI",
                    "aws:cloudformation:stack-id": "arn:aws:cloudformation:us-west-2:758325631830:stack/aesd/0978dd20-ca90-11ec-8e6f-06f0b04d699d",
                    "aws:cloudformation:stack-name": "aesd"
                },
                "cost_for_month": "3.50 USD"
            }
        },
        {
            "data": {
                "id": "arn:aws:execute-api:us-west-2:758325631830:9z24ydgzs2",
                "arn": "arn:aws:execute-api:us-west-2:758325631830:9z24ydgzs2",
                "type": "API Gateway",
                "name": "GetJsonFromS3",
                "account_id": "758325631830",
                "region": "us-west-2",
                "resource": [
                    {
                        "id": "9hzbjs0icg",
                        "path": "/",
                        "resourceMethods": {
                            "GET": {},
                            "OPTIONS": {}
                        }
                    }
                ],
                "tag": {
                    "aws:cloudformation:logical-id": "PerspectiveDrawioWebRestAPI",
                    "aws:cloudformation:stack-id": "arn:aws:cloudformation:us-west-2:758325631830:stack/aesd/0978dd20-ca90-11ec-8e6f-06f0b04d699d",
                    "aws:cloudformation:stack-name": "aesd"
                },
                "cost_for_month": "3.50 USD"
            }
        },
        {
            "data": {
                "id": "arn:aws:execute-api:us-west-2:758325631830:fre4xd47rj",
                "arn": "arn:aws:execute-api:us-west-2:758325631830:fre4xd47rj",
                "type": "API Gateway",
                "name": "PostUserToDynamo",
                "account_id": "758325631830",
                "region": "us-west-2",
                "resource": [
                    {
                        "id": "8v7pzrsddc",
                        "path": "/",
                        "resourceMethods": {
                            "OPTIONS": {},
                            "POST": {}
                        }
                    }
                ],
                "tag": {
                    "aws:cloudformation:logical-id": "PerspectiveDrawioWebRestAPI",
                    "aws:cloudformation:stack-id": "arn:aws:cloudformation:us-west-2:758325631830:stack/aesd/0978dd20-ca90-11ec-8e6f-06f0b04d699d",
                    "aws:cloudformation:stack-name": "aesd"
                },
                "cost_for_month": "3.50 USD"
            }
        },
        {
            "data": {
                "id": "arn:aws:execute-api:us-west-2:758325631830:p0ro5huich",
                "arn": "arn:aws:execute-api:us-west-2:758325631830:p0ro5huich",
                "type": "API Gateway",
                "name": "MySfn",
                "account_id": "758325631830",
                "region": "us-west-2",
                "resource": [
                    {
                        "id": "jgzeuth18a",
                        "path": "/",
                        "resourceMethods": {
                            "GET": {},
                            "OPTIONS": {},
                            "POST": {}
                        }
                    }
                ],
                "tag": {
                    "aws:cloudformation:logical-id": "PerspectiveDrawioWebRestAPI",
                    "aws:cloudformation:stack-id": "arn:aws:cloudformation:us-west-2:758325631830:stack/aesd/0978dd20-ca90-11ec-8e6f-06f0b04d699d",
                    "aws:cloudformation:stack-name": "aesd"
                },
                "cost_for_month": "3.50 USD"
            }
        },
        {
            "data": {
                "id": "arn:aws:execute-api:us-west-2:758325631830:vdl1vfjdg9",
                "arn": "arn:aws:execute-api:us-west-2:758325631830:vdl1vfjdg9",
                "type": "API Gateway",
                "name": "testAPI",
                "account_id": "758325631830",
                "region": "us-west-2",
                "resource": [
                    {
                        "id": "0191pg",
                        "parentId": "at5c28y3n8",
                        "pathPart": "execution",
                        "path": "/execution",
                        "resourceMethods": {
                            "POST": {}
                        }
                    },
                    {
                        "id": "at5c28y3n8",
                        "path": "/"
                    }
                ],
                "tag": {
                    "aws:cloudformation:logical-id": "PerspectiveDrawioWebRestAPI",
                    "aws:cloudformation:stack-id": "arn:aws:cloudformation:us-west-2:758325631830:stack/aesd/0978dd20-ca90-11ec-8e6f-06f0b04d699d",
                    "aws:cloudformation:stack-name": "aesd"
                },
                "cost_for_month": "3.50 USD"
            }
        },
        {
            "data": {
                "id": "arn:aws:execute-api:us-west-2:758325631830:vrnkwss7h0",
                "arn": "arn:aws:execute-api:us-west-2:758325631830:vrnkwss7h0",
                "type": "API Gateway",
                "name": "CloudDayOneAPI",
                "account_id": "758325631830",
                "region": "us-west-2",
                "resource": [
                    {
                        "id": "bjzqsn",
                        "parentId": "efmilo5s6f",
                        "pathPart": "greeting",
                        "path": "/greeting"
                    },
                    {
                        "id": "efmilo5s6f",
                        "path": "/",
                        "resourceMethods": {
                            "GET": {},
                            "OPTIONS": {},
                            "POST": {}
                        }
                    }
                ],
                "tag": {
                    "aws:cloudformation:logical-id": "PerspectiveDrawioWebRestAPI",
                    "aws:cloudformation:stack-id": "arn:aws:cloudformation:us-west-2:758325631830:stack/aesd/0978dd20-ca90-11ec-8e6f-06f0b04d699d",
                    "aws:cloudformation:stack-name": "aesd"
                },
                "cost_for_month": "3.50 USD"
            }
        },
        {
            "data": {
                "id": "arn:aws:execute-api:us-west-2:758325631830:zk0oea00u9",
                "arn": "arn:aws:execute-api:us-west-2:758325631830:zk0oea00u9",
                "type": "API Gateway",
                "name": "step_funcation",
                "account_id": "758325631830",
                "region": "us-west-2",
                "resource": [
                    {
                        "id": "1k95ds",
                        "parentId": "k6lwvk7le7",
                        "pathPart": "ListUserInformation",
                        "path": "/ListUserInformation",
                        "resourceMethods": {
                            "ANY": {}
                        }
                    },
                    {
                        "id": "drjou9",
                        "parentId": "k6lwvk7le7",
                        "pathPart": "test",
                        "path": "/test",
                        "resourceMethods": {
                            "GET": {},
                            "OPTIONS": {},
                            "POST": {}
                        }
                    },
                    {
                        "id": "k6lwvk7le7",
                        "path": "/",
                        "resourceMethods": {
                            "GET": {},
                            "OPTIONS": {},
                            "POST": {}
                        }
                    }
                ],
                "tag": {
                    "aws:cloudformation:logical-id": "PerspectiveDrawioWebRestAPI",
                    "aws:cloudformation:stack-id": "arn:aws:cloudformation:us-west-2:758325631830:stack/aesd/0978dd20-ca90-11ec-8e6f-06f0b04d699d",
                    "aws:cloudformation:stack-name": "aesd"
                },
                "cost_for_month": "3.50 USD"
            }
        },
        {
            "data": {
                "id": "us-west-2:18ec6d79-caab-4c59-9469-94a534661ee1",
                "arn": "us-west-2:18ec6d79-caab-4c59-9469-94a534661ee1",
                "type": "Cognito",
                "name": "Clouday1",
                "account_id": "758325631830",
                "region": "us-west-2",
                "cost_for_month": "0.00 USD",
                "IdentityPoolId": "us-west-2:18ec6d79-caab-4c59-9469-94a534661ee1",
                "IdentityPoolName": "Clouday1",
                "AllowUnauthenticatedIdentities": true,
                "AllowClassicFlow": false,
                "ResponseMetadata": {
                    "RequestId": "95d58869-b867-4f28-ab87-e376ec061f68",
                    "HTTPStatusCode": 200,
                    "HTTPHeaders": {
                        "date": "Wed, 25 May 2022 03:35:48 GMT",
                        "content-type": "application/x-amz-json-1.1",
                        "content-length": "343",
                        "connection": "keep-alive",
                        "x-amzn-requestid": "95d58869-b867-4f28-ab87-e376ec061f68"
                    },
                    "RetryAttempts": 0
                },
                "tag": {
                    "Application": "web",
                    "Department": "Intership",
                    "Environment": "Prod",
                    "Owner": "Front-end",
                    "Project": "Clouday1",
                    "PutVideoToS3": "audio-jason",
                    "UseSns": "",
                    "clouday1": ""
                }
            }
        },
        {
            "data": {
                "id": "us-west-2:367b07c8-2d2d-4cc5-855d-8f537211b8f6",
                "arn": "us-west-2:367b07c8-2d2d-4cc5-855d-8f537211b8f6",
                "type": "Cognito",
                "name": "Clouday1_translate",
                "account_id": "758325631830",
                "region": "us-west-2",
                "cost_for_month": "0.00 USD",
                "IdentityPoolId": "us-west-2:367b07c8-2d2d-4cc5-855d-8f537211b8f6",
                "IdentityPoolName": "Clouday1_translate",
                "AllowUnauthenticatedIdentities": true,
                "AllowClassicFlow": false,
                "ResponseMetadata": {
                    "RequestId": "0271ff3f-1552-4aac-bce4-ed0dc72d8b65",
                    "HTTPStatusCode": 200,
                    "HTTPHeaders": {
                        "date": "Wed, 25 May 2022 03:35:48 GMT",
                        "content-type": "application/x-amz-json-1.1",
                        "content-length": "192",
                        "connection": "keep-alive",
                        "x-amzn-requestid": "0271ff3f-1552-4aac-bce4-ed0dc72d8b65"
                    },
                    "RetryAttempts": 0
                },
                "tag": {}
            }
        },
        {
            "data": {
                "id": "us-west-2:5389609a-ca44-4abf-a418-ef6c92f906b4",
                "arn": "us-west-2:5389609a-ca44-4abf-a418-ef6c92f906b4",
                "type": "Cognito",
                "name": "MyTrans",
                "account_id": "758325631830",
                "region": "us-west-2",
                "cost_for_month": "0.00 USD",
                "IdentityPoolId": "us-west-2:5389609a-ca44-4abf-a418-ef6c92f906b4",
                "IdentityPoolName": "MyTrans",
                "AllowUnauthenticatedIdentities": true,
                "AllowClassicFlow": false,
                "ResponseMetadata": {
                    "RequestId": "5a30b472-3564-4602-9833-fb60ed8ac58d",
                    "HTTPStatusCode": 200,
                    "HTTPHeaders": {
                        "date": "Wed, 25 May 2022 03:35:48 GMT",
                        "content-type": "application/x-amz-json-1.1",
                        "content-length": "181",
                        "connection": "keep-alive",
                        "x-amzn-requestid": "5a30b472-3564-4602-9833-fb60ed8ac58d"
                    },
                    "RetryAttempts": 0
                },
                "tag": {}
            }
        },
        {
            "data": {
                "type": "RDS",
                "id": "arn:aws:rds:us-west-2:758325631830:db:rds-1",
                "arn": "arn:aws:rds:us-west-2:758325631830:db:rds-1",
                "name": "rds-1",
                "account_id": "758325631830",
                "region": "us-west-2",
                "engine_type": "mysql",
                "instance_type": "db.t3.micro",
                "storage_type": "gp2",
                "launch_time": "2022-05-24T09:30:51.240000+00:00",
                "instance_status": "stopped",
                "vpc": "sg-02426d558db9c54dd",
                "tag": {
                    "Project": "Cloudtest",
                    "Environment": "Test",
                    "Department": "Atlas",
                    "Owner": "Back-end",
                    "Application": "processing"
                },
                "cost_for_month": "14.4 USD"
            }
        },
        {
            "data": {
                "type": "RDS",
                "id": "arn:aws:rds:us-west-2:758325631830:db:rds-2",
                "arn": "arn:aws:rds:us-west-2:758325631830:db:rds-2",
                "name": "rds-2",
                "account_id": "758325631830",
                "region": "us-west-2",
                "engine_type": "postgres",
                "instance_type": "db.t3.micro",
                "storage_type": "gp2",
                "launch_time": "2022-05-24T20:49:23.148000+00:00",
                "instance_status": "stopped",
                "vpc": "sg-02426d558db9c54dd",
                "tag": {
                    "Project": "Cloudaytest",
                    "Department": "Atlas",
                    "Owner": "Back-end",
                    "Enviroment": "Test",
                    "Application": "processing"
                },
                "cost_for_month": "14.4 USD"
            }
        },
        {
            "data": {
                "id": "arn:aws:ec2:us-west-2:758325631830:instance/i-0fa4c259cdb1c0ec6",
                "arn": "arn:aws:ec2:us-west-2:758325631830:instance/i-0fa4c259cdb1c0ec6",
                "type": "EC2",
                "name": "Neo4j",
                "account_id": "758325631830",
                "region": "us-west-2",
                "LaunchTime": "2022-04-01T09:49:56+00:00",
                "InstanceType": "t2.micro",
                "tag": {
                    "Name": "neo4j"
                },
                "cost_for_month": "64.54 USD"
            }
        },
        {
            "data": {
                "id": "arn:aws:ec2:us-west-2:758325631830:instance/i-0afd7bcb3a00bca51",
                "arn": "arn:aws:ec2:us-west-2:758325631830:instance/i-0afd7bcb3a00bca51",
                "type": "EC2",
                "name": "cloudDay1keypair",
                "account_id": "758325631830",
                "region": "us-west-2",
                "LaunchTime": "2022-03-22T18:47:44+00:00",
                "InstanceType": "t2.micro",
                "tag": {
                    "Name": "EC2-MySQL"
                },
                "cost_for_month": "64.54 USD"
            }
        },
        {
            "data": {
                "id": "arn:aws:ec2:us-west-2:758325631830:instance/i-08e41dc2ea3da1a9f",
                "arn": "arn:aws:ec2:us-west-2:758325631830:instance/i-08e41dc2ea3da1a9f",
                "type": "EC2",
                "name": "cloudDay1keypair",
                "account_id": "758325631830",
                "region": "us-west-2",
                "LaunchTime": "2022-04-19T06:44:04+00:00",
                "InstanceType": "t2.micro",
                "tag": {
                    "Name": "ec2_one"
                },
                "cost_for_month": "64.54 USD"
            }
        },
        {
            "data": {
                "id": "arn:aws:ec2:us-west-2:758325631830:instance/i-0ae5c0c264c665b21",
                "arn": "arn:aws:ec2:us-west-2:758325631830:instance/i-0ae5c0c264c665b21",
                "type": "EC2",
                "name": "cloudDay1keypair",
                "account_id": "758325631830",
                "region": "us-west-2",
                "LaunchTime": "2022-04-02T04:13:34+00:00",
                "InstanceType": "t2.micro",
                "tag": {
                    "Name": "neo4jnewdb"
                },
                "cost_for_month": "64.54 USD"
            }
        },
        {
            "data": {
                "id": "arn:aws:ec2:us-west-2:758325631830:instance/i-0d7475fdfc72fef90",
                "arn": "arn:aws:ec2:us-west-2:758325631830:instance/i-0d7475fdfc72fef90",
                "type": "EC2",
                "name": "clouday1_web_server",
                "account_id": "758325631830",
                "region": "us-west-2",
                "LaunchTime": "2022-05-25T02:11:05+00:00",
                "InstanceType": "t2.micro",
                "tag": {
                    "Application": "processing",
                    "Project": "Architecture",
                    "Department": "Intership",
                    "Environment": "Pre-Prod",
                    "Owner": "Back-end",
                    "Name": "clouday1_web_server"
                },
                "cost_for_month": "64.54 USD"
            }
        },
        {
            "data": {
                "id": "arn:aws:ec2:us-west-2:758325631830:instance/i-0e7b3e5bee6743c51",
                "arn": "arn:aws:ec2:us-west-2:758325631830:instance/i-0e7b3e5bee6743c51",
                "type": "EC2",
                "name": "nginx",
                "account_id": "758325631830",
                "region": "us-west-2",
                "LaunchTime": "2022-04-28T02:33:00+00:00",
                "InstanceType": "t2.micro",
                "tag": {
                    "Name": "nginx"
                },
                "cost_for_month": "64.54 USD"
            }
        },
        {
            "data": {
                "id": "arn:aws:ec2:us-west-2:758325631830:instance/i-0f07c4b167dd9c7c7",
                "arn": "arn:aws:ec2:us-west-2:758325631830:instance/i-0f07c4b167dd9c7c7",
                "type": "EC2",
                "name": "ArchWebServer_Keypair",
                "account_id": "758325631830",
                "region": "us-west-2",
                "LaunchTime": "2022-05-04T01:37:33+00:00",
                "InstanceType": "t2.micro",
                "tag": {
                    "Name": "Arch-Web-Server"
                },
                "cost_for_month": "64.54 USD"
            }
        },
        {
            "data": {
                "id": "arn:aws:ec2:us-west-2:758325631830:instance/i-0504c0972ed726015",
                "arn": "arn:aws:ec2:us-west-2:758325631830:instance/i-0504c0972ed726015",
                "type": "EC2",
                "name": "ArchWebServer_Keypair",
                "account_id": "758325631830",
                "region": "us-west-2",
                "LaunchTime": "2022-05-05T03:35:59+00:00",
                "InstanceType": "t2.micro",
                "tag": {
                    "Name": "Arch-Web"
                },
                "cost_for_month": "64.54 USD"
            }
        },
        {
            "data": {
                "id": "arn:aws:ec2:us-west-2:758325631830:instance/i-090121e3a195ba77a",
                "arn": "arn:aws:ec2:us-west-2:758325631830:instance/i-090121e3a195ba77a",
                "type": "EC2",
                "name": "clouday1_web_server",
                "account_id": "758325631830",
                "region": "us-west-2",
                "LaunchTime": "2022-05-18T02:34:28+00:00",
                "InstanceType": "t2.micro",
                "tag": {
                    "Name": "Vue-Web-Server"
                },
                "cost_for_month": "64.54 USD"
            }
        },
        {
            "data": {
                "id": "arn:aws:ec2:us-west-2:758325631830:instance/i-0c503566368805b3a",
                "arn": "arn:aws:ec2:us-west-2:758325631830:instance/i-0c503566368805b3a",
                "type": "EC2",
                "name": "clouday1_web_server",
                "account_id": "758325631830",
                "region": "us-west-2",
                "LaunchTime": "2022-05-18T02:36:00+00:00",
                "InstanceType": "t2.micro",
                "tag": {
                    "Department": "Intership",
                    "Application": "processing",
                    "Owner": "Back-end",
                    "Environment": "Pre-Prod",
                    "Name": "Vue-arch-web-server",
                    "Project": "Architecture"
                },
                "cost_for_month": "64.54 USD"
            }
        },
        {
            "data": {
                "id": "arn:aws:ec2:us-west-2:758325631830:instance/i-0ed2b2c3b55eb4f7d",
                "arn": "arn:aws:ec2:us-west-2:758325631830:instance/i-0ed2b2c3b55eb4f7d",
                "type": "EC2",
                "name": "cloudDay1keypair",
                "account_id": "758325631830",
                "region": "us-west-2",
                "LaunchTime": "2022-03-30T03:59:16+00:00",
                "InstanceType": "t2.micro",
                "tag": {
                    "Name": "test-api-call-step"
                },
                "cost_for_month": "64.54 USD"
            }
        },
        {
            "data": {
                "id": "arn:aws:ec2:us-west-2:758325631830:instance/i-040cf39751eb72c0a",
                "arn": "arn:aws:ec2:us-west-2:758325631830:instance/i-040cf39751eb72c0a",
                "type": "EC2",
                "name": "cloudDay1keypair",
                "account_id": "758325631830",
                "region": "us-west-2",
                "LaunchTime": "2022-04-01T09:37:01+00:00",
                "InstanceType": "m4.large",
                "tag": {
                    "Name": ""
                },
                "cost_for_month": "64.54 USD"
            }
        },
        {
            "data": {
                "id": "arn:aws:ec2:us-west-2:758325631830:instance/i-02ff498f6271bda47",
                "arn": "arn:aws:ec2:us-west-2:758325631830:instance/i-02ff498f6271bda47",
                "type": "EC2",
                "name": "chen",
                "account_id": "758325631830",
                "region": "us-west-2",
                "LaunchTime": "2022-03-22T10:03:20+00:00",
                "InstanceType": "t2.micro",
                "tag": {
                    "Name": "testSecurityGroup"
                },
                "cost_for_month": "64.54 USD"
            }
        },
        {
            "data": {
                "id": "arn:aws:ec2:us-west-2:758325631830:instance/i-04850a0016b6718f2",
                "arn": "arn:aws:ec2:us-west-2:758325631830:instance/i-04850a0016b6718f2",
                "type": "EC2",
                "name": "cloudDay1keypair",
                "account_id": "758325631830",
                "region": "us-west-2",
                "LaunchTime": "2022-04-19T06:44:19+00:00",
                "InstanceType": "t2.micro",
                "tag": {
                    "Name": "ec2_two"
                },
                "cost_for_month": "64.54 USD"
            }
        },
        {
            "data": {
                "id": "arn:aws:ec2:us-west-2:758325631830:instance/i-0e24942520cb83036",
                "arn": "arn:aws:ec2:us-west-2:758325631830:instance/i-0e24942520cb83036",
                "type": "EC2",
                "name": "Neo4j Key",
                "account_id": "758325631830",
                "region": "us-west-2",
                "LaunchTime": "2022-04-05T15:16:25+00:00",
                "InstanceType": "t2.micro",
                "tag": {
                    "Name": "Neo4j Demo"
                },
                "cost_for_month": "64.54 USD"
            }
        }
    ],[])