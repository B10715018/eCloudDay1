from utils.lambda_get_policy import lambda_get_policy
from utils.lambda_list_function import lambda_list_function
from utils.sqs_list_queue import sqs_list_queue
from utils.sqs_get_queue import sqs_get_queue

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


# initialize class
collect_command = Collect(REGION_NAME)

# call command functions
collect_command.get_lambda_list()
collect_command.get_lambda_policy()
collect_command.list_sqs_queue()
collect_command.get_sqs_queue()
