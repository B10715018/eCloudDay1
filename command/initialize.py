from clouday1_extract_aws_metadata import ddb_initial_request
from clouday1_extract_aws_metadata import process_input_from_front
from clouday1_extract_aws_metadata import send_request_to_s3
from clouday1_extract_aws_metadata import iam_get_caller_identity

class Initialize:
    '''Initialize the request and validate the aws credentials'''
    def __init__(self):
        self.region_name=[]
        self.account_id=''
        self.account_name=''
        self.aws_access_key_id=''
        self.aws_secret_access_key=''
        self.aws_session_token=''
    def print_class_parameter(self):
        print(self.account_id)
        print(self.account_name)
        print(len(self.region_name))
        print(self.aws_access_key_id)
        print(self.aws_secret_access_key)
        print(self.aws_session_token)
    def validate_input(self):
        input=process_input_from_front.processing_input_from_front_end()
        if(input['region']):
            self.region_name=input['region']
        if(input['account_name']):
            self.account_name=input['account_name']
        if(input['aws_access_key_id']):
            self.aws_access_key_id=input['aws_access_key_id']
        if(input['aws_secret_access_key']):
            self.aws_secret_access_key=input['aws_secret_access_key']
        if(input['aws_session_token']):
            self.aws_session_token=input['aws_session_token']
    def check_identity(self):
        account_id=iam_get_caller_identity.get_account_id(self.aws_access_key_id,
            self.aws_secret_access_key,self.region_name[0])
        self.account_id=account_id
    def send_request_to_s3(self):
        send_request_to_s3.send_request_to_s3(self.account_name)
    def make_request(self):
        ddb_initial_request.initial_request_to_ddb(self.region_name,self.account_id)


# make class instance
initialize_command=Initialize()
# execute class function
initialize_command.validate_input()
initialize_command.check_identity()
initialize_command.send_request_to_s3()
initialize_command.make_request()
initialize_command.print_class_parameter()