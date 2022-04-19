from utils.lambda_get_policy import lambda_get_policy
from utils.lambda_list_function import lambda_list_function

from utils.dynamodb_list_table import dynamodb_list_table

from utils.s3_list_bucket import s3_list_bucket 
from utils.s3_get_bucket_policy import s3_get_bucket_policy


class Collect:
    '''Collect class for collecting data from AWS Lambda'''

    def __init__(self, region_name):
        self.region_name = region_name

    def get_lambda_list(self):
        lambda_list_function()

    def get_lambda_policy(self):
        lambda_get_policy()

    def list_dynamodb_table(self):
        dynamodb_list_table()

    def list_s3_bucket(self):
        s3_list_bucket()
        
    def get_s3_bucket_policy(self):
        s3_get_bucket_policy

# initialize class
collect_command = Collect('us-west-2')

collect_command.get_lambda_list()
collect_command.get_lambda_policy()

collect_command.list_dynamodb_table()
collect_command.list_s3_bucket()
collect_command.get_s3_bucket_policy
