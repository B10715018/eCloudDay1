from utils.lambda_get_policy import lambda_get_policy
from utils.lambda_list_function import lambda_list_function
from utils.sqs_list_queue import sqs_list_queue
from utils.sqs_get_queue import sqs_get_queue

'''Collect class for collecting data from AWS Lambda'''


class Collect:
    '''Collect class for collecting data from AWS Lambda'''

    def __init__(self, region_name):
        self.region_name = region_name

    def get_lambda_list(self):
        lambda_list_function()

    def get_lambda_policy(self):
        lambda_get_policy()

    def list_sqs_queue(self):
        sqs_list_queue()

    def get_sqs_queue(self):
        sqs_get_queue()


# initialize class
collect_command = Collect('us-west-2')

collect_command.get_lambda_list()
collect_command.get_lambda_policy()
collect_command.list_sqs_queue()
collect_command.get_sqs_queue()
