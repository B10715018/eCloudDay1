from utils.lambda_get_policy import lambda_get_policy
from utils.lambda_list_function import lambda_list_function
from utils.sqs_list_queue import sqs_list_queue
from utils.sqs_get_queue import sqs_get_queue
from utils.sns_list_topic import sns_list_topic
from utils.sns_get_topic_attribute import sns_get_topic_attribute
from utils.dynamodb_list_table import dynamodb_list_table
from utils.dynamodb_scan import dynamodb_scan
from utils.cloudtrail_sfn_start_execution import cloudtrail_start_sfn

'''Collect class for collecting data from AWS Lambda'''

REGION_NAME = 'us-west-2'


class Collect:
    '''Collect class for collecting data from AWS Lambda'''

    def __init__(self, region_name):
        self.region_name = region_name

    def get_lambda_list(self):
        lambda_list_function(self.region_name)

    def get_lambda_policy(self):
        lambda_get_policy(self.region_name)

    def list_sqs_queue(self):
        sqs_list_queue(self.region_name)

    def get_sqs_queue(self):
        sqs_get_queue(self.region_name)

    def list_sns_topic(self):
        sns_list_topic(self.region_name)

    def get_sns_topic_attribute(self):
        sns_get_topic_attribute(self.region_name)

    def list_dynamodb_table(self):
        dynamodb_list_table(self.region_name)

    def scan_dynamodb_table(self):
        dynamodb_scan(self.region_name)

    def get_cloudtrail_start_sfn(self):
        cloudtrail_start_sfn(self.region_name)


# initialize class
collect_command = Collect(REGION_NAME)

# call command functions
collect_command.get_lambda_list()
collect_command.get_lambda_policy()
collect_command.list_sqs_queue()
collect_command.get_sqs_queue()
collect_command.list_sns_topic()
collect_command.get_sns_topic_attribute()
collect_command.list_dynamodb_table()
collect_command.scan_dynamodb_table()
collect_command.get_cloudtrail_start_sfn()
