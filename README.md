# eCloudDay1

## Steps on how to use:

1. Clone your repository:
   git clone https://github.com/B10715018/eCloudDay1.git

2. Create virtual environment and activate it:

   python3 -m venv ./venv && source venv/bin/activate

3. Install the dependencies:
   pip install -r requirements.txt

4. Don't forget to configure your account:
   aws configure --profile

5. To use some functionality, for example scan dynamodb:
   python dynamodb-scan.py

6. Results data can be obtained in the 'data' folder

7. Please create a folder name 'data' at the eCloudDay1 repositories it is where we could store all metadata in form of JSON

## Instruction to run script file:

1. make sure you have the 'job.sh' file in your directory

2. execute this command in your terminal `chmod u+x job.sh`

3. run it using this command in your terminal `./job.sh`, run it 2 times to ensure there is no missing data

## Github Action Workflow

1. This is to automate checking test on every python file made.

2. If there is error it will return failed test and will send email of failed test to the contributor who pushed or pull the request

3. If all checks are passed, you may continue to create a pull request or else you need to fix your code first

# THANK YOU
