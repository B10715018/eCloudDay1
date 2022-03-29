import boto3
import json

client=boto3.client('stepfunctions',region_name='us-west-2')

response = client.list_executions(
  stateMachineArn='arn:aws:states:us-west-2:758325631830:stateMachine:lambda')

# print(response)

response2=client.describe_execution(
  executionArn='arn:aws:states:us-west-2:758325631830:execution:lambda:2d5a6152-1f9a-4fb7-b6f9-692d0b752963'
)

print(response2)