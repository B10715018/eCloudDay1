import boto3
from boto3.dynamodb.conditions import  Key
def process_requestID(requestID):
    status_code=None
    message= None
    try:
            # initiliaze dynamodb request
            dynamodb = boto3.resource('dynamodb')
            table = dynamodb.Table('architectureDB')
            # query the table based on the requestID partition key
            response = table.query(
                KeyConditionExpression=Key('requestID').eq(requestID)
                )
            # pass the items
            items=response['Items'][0]
            account_name=items['account_name']
            print(account_name)
            status_code=200
            message=account_name
    # if unexpected error happened      
    except:
        status_code = 500
        message = "Bad Error Request"
    
    finally:
        return {
            "status_code": status_code,
            "message": message
        }
