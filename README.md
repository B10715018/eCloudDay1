# eCloudDay1 :sun_behind_large_cloud:

## Steps on how to use:

1. Clone your repository:
   ```
   git clone https://github.com/B10715018/eCloudDay1.git
   ```

2. Create virtual environment and activate it:

   ```
   python3 -m venv ./venv && source venv/bin/activate
   ```

3. Install the dependencies:
   ```
   pip3 install -r requirements.txt
   ```

4. Don't forget to configure your account:
   ```
   aws configure --profile
   ```

5. To use some functionality, for example scan dynamodb:
   ```
   python dynamodb-scan.py
   ```

6. Results data can be obtained in the `data` folder

7. Please create a folder name `data` at the eCloudDay1 repositories it is where we could store all metadata in form of JSON

## Publish `clouday1_extract_aws_metadata` into python package

1. To Publish python package file make sure you have `twine` in your virtual environment: execute 
```
pip3 install setuptools twine
```
2. Create a distribution folder for our python package by executing 
```
python3 setup.py sdist
```
3. Upload your package folder into PyPi repository by executing : 
```
twine upload --repository-url https://upload.pypi.org/legacy dist/* 
```
4. You will be asked to insert your username and password for PyPi account to upload the package to PyPi repositories
5. Then you can view our package here:[Own Built Clouday1 Package](https://pypi.org/project/clouday1-extract-aws-metadata/0.0.1/)

Reference Video can be found here : [Reference Video Tutorial](https://www.youtube.com/watch?v=zhpI6Yhz9_4)

## New Version (OOP Version)

1. The design of class diagram can be find in `docs` folder in [Diagram](docs/classdiagram.png)

## Instruction to run `collect.py` file:

1. make sure you have the 'job.sh' file in your directory

2. execute this command in your terminal 
```
chmod u+x job.sh
```

3. run it using this command in your terminal `./job.sh`, run it 2 times to ensure there is no missing data

## To run `prepare.py` file:

1. make sure you have 'job2.sh' file in your directory

2. execute this command in your terminal 
```
chmod u+x job2.sh
```

3. run it using this command in your terminal 
```
./job2.sh
```

## Added some extra function to clear all JSON file in ./data folder:

1. make sure you have `jobClearJSON.sh` file in your directory

2. execute this command in your terminal 
```
chmod u+x jobClearJSON.sh
```

3. run it using this command in your terminal 
```
./jobClearJSON.sh
```

## Github Action Workflow

1. This is to automate checking test on every python file made.

2. If there is error it will return failed test and will send email of failed test to the contributor who pushed or pull the request

3. If all checks are passed, you may continue to create a pull request or else you need to fix your code first


# THANK YOU
