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
## New Version (OOP Version)

1. The design of class diagram can be find in `docs` folder in [Diagram](docs/classdiagram.png)

## Extra tool to clear all JSON file in `data` folder:

1. make sure you have `jobClearJSON.sh` file in your directory

2. execute this command in your terminal 
```
chmod u+x ./tools/shell/jobClearJSON.sh
```

3. run it using this command in your terminal 
```
./tools/shell/jobClearJSON.sh
```

## Github Action Workflow

1. This is to automate checking test on every python file made.

2. If there is error it will return failed test and will send email of failed test to the contributor who pushed or pull the request

3. If all checks are passed, you may continue to create a pull request or else you need to fix your code first
## Documentation on how to publish new Python Package to PYPI
[Link to learn how to publish new Python package to PYPI](./docs/publish_new_python_package.md)
## Documentation for migrating local to AWS Environment
[Link to deploy to AWS from local](./docs/migrate_local_to_AWS_env.md)
## Documentation for automation ton upload to PYPI repositories
[Link to deploy to PYPI repositories](./docs/deploy_to_pypi_script.md)
## Documentation for Docker Container and ECS could be found here
[Link to Docker and ECS Documentation](./docs/dockertoECS.md)

## Documentation on how to update the PYPI package
[Link to Tutorial to update PYPI Package](./docs/updatePythonPackage.md)
## Reference
- [How to setup nginx, gunicorn(WGSI) and Django tutorial](https://www.youtube.com/watch?v=I4eN7QQzKd0) 

- [Setup bootstrap for EC2](https://stackoverflow.com/questions/55471199/how-to-start-gunicorn-on-startup-ec2-instance)

- [Nginx Documentation](https://nginx.org/en/docs/)

- [Gunicorn Documentation](https://docs.gunicorn.org/en/stable/configure.html)

- [Flask Documentation](https://flask.palletsprojects.com/en/2.1.x/)

- [How to dockerize app and deploy to Fargate](https://towardsdatascience.com/deploying-a-docker-container-with-ecs-and-fargate-7b0cbc9cd608)

- [Scripting Techniques](https://www.serverlab.ca/tutorials/linux/administration-linux/how-to-set-environment-variables-in-linux/)
# THANK YOU :heart:
