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

## Migrate Project from local to AWS environment

### Set EC2 Instance

1. Go to your AWS Console and go to `EC2` console

2. Click `Launch Instance` in the `EC2` console 

3. Choose `Ubuntu Server 20.04 LTS (HVM), SSD Volume Type 64-bit (x86) ` for AMI

4. For instance type choose `t2.micro`

5. Click `Review and Launch`, then click `Launch` on the `Review` Page

6. For keypair, you can choose either to create your own key pair or select existing key pair

7. Finally Click `Launch Instance`

### SSH to EC2 instance

1. Go to your terminal

2. Execute this command to ensure key is not publicly viewable:
```
chmod 400 {YOUR_KEY_PAIR_NAME}.pem
```
3. Connect to EC2 through SSH Client
```  
ssh -i "{YOUR_KEY_PAIR_NAME}.pem" ubuntu@ec2-{YOUR-IP-ADDRESS}.us-west-2.compute.amazonaws.com
```

### After Connecting to EC2 instance, set up the instance environment make sure nginx is running

1. First inside the EC2 instance terminal, run:
```
sudo apt update
```
Extra info : `apt` is a package manager, the command above is to make sure that the package manager is up to date

2. Install the nginx webserver inside the EC2 terminal, run:
```
sudo apt-get install nginx
```

3. Make sure that we have nginx web server running, execute:
- Change your directory into `/etc/nginx`:
```
cd /etc/nginx
```
- In the current directory,execute this command :
```
sudo systemctl start nginx
```
Extra info : `systemctl` is system control is used to provide interface for user to control system inside instance
The command above is used to start the nginx webserver inside your instance

4. Open your public IPV4 address in the internet:
You will found out that EC2 instance server cannot connect to the internet, because by default the security group that
we just made block all inbound request and allow all outbound request. So we need to configure our security group

5. Setup our security group to allow inbound:

- In the `EC2` console choose your instance id

- Choose and Click on the `Security Groups`

- Click on the `Edit inbound rules`

- Then click on `add rule`, choose `Custom TCP` for Type, fill `80` in Port Range and choose `Anywhere` for Source, this is used 
  to open HTTP port(80)

- Next, click on `add rule`, choose `Custom TCP` for Type, fill `443` in Port Range and choose `Anywhere` for Source, this is used
  to open HTTPS Port(443)

- Last , click on `add rule`, choose `Custom TCP` for Type, fill `9000` in Port Range and choose `Anywhere` for Source, this is used
  to open the app which we host on Port 9000

- Then click on `Save Rules`

6. Now if we open the public IPV4 address, we could see the nginx web server is up and running

### Setup important tools that is needed for our app
 1. Install pip python package manager by executing:
 ```
 sudo apt install python3-pip
 ```
 2. Install virtual env tool in python3:
 ```
 sudo apt install python3.8-venv
 ```
 3. Install AWS Cli tool:
 ```
 sudo apt-get install awscli
 ```

 4. Create new directory in your instance:
 ```
 mkdir project2
 ```
 5. Go to currently created directory:
```
cd project2
```
6. Ask Project Owner for Personal Access Token to clone project repository
7. Clone the github repository in the EC2 instance terminal
```
git clone https://github.com/B10715018/eCloudDay1.git`
```
8. Enter the username and PAT after executing the previous command
9. Execute `ls` and make sure that the clone repository is inside your ec2 instance
10. Go to our project directory by executing:
```
cd eCloudDay1
```
11. Create virtual environment and activate the virtual environment
```
python3 -m venv ./venv && source venv/bin/activate
```
12. Install the dependencies in the `venv`
```
pip3 install -r requirements.txt && pip3 install wheel
```
13. Configure your AWS Account in the EC2 terminal
```
aws configure
```
14. Insert your AWS Access ID , Secret Access Key and region set into `us-west-2`
15. And we are done setting important tools for our app

### Component inside the app
#### Flask app
1. Our Flask app can be find in [Flask app](./app.py)
2. This route are used to determine where the request will come determing their method
   `(POST,GET,DELETE,PUT)` and their resource path, i.e. `http://{your_ec2_ip_address}/{resource_path}`
3. As for now these are the routes for our app:
   - Method :`ANY`
      `/` : will redirect you to a page showing `Hello World`
   - Method: `POST`
      `/collect`: will redirect you to trigger the collection of all metadata in `collect.py`
   - Method: `POST` 
      `/prepare`: will redirect you to trigger to prepare the `data.json` file
   - Method: `DELETE`
      `/request`: will redirect you to trigger the job to clear all files in the `data` folder
4. Finally our app will run in Port 9000 as seen in the bottom of `app.py` file

#### WSGI Server
1. WSGI : Web Server Gateway Interface is the interface for the webserver and it will be bind with gunicorn to serve many workers inside the EC2 instance to ensure that our app still could run if a worker failed to process request

2. The configuration settings can be found in [WSGI](./wsgi.py)

#### NGINX Web Server
1. It is used to receive and pass request coming in and out of EC2 instance
2. For configuration, go back to the root directory of EC2 instance terminal
3. Execute this command to go to the nginx configuration directory:
```
cd /etc/nginx/sites-enabled/
```
4. Execute `ls` in the current directory, make sure `default` file is there
5. Let us do some editing in the `default` file by executing:
```
sudo vi default
```
6. Inside the editor press `i` to insert data and comment the `try_files $uri $uri/ =404;` at the `location` section
7. Add `proxy_pass http://{host_address}:{PORT}` in the `location` section
8. To exit press `esc` and type `:wq` to quit and save from editor

### Setup gunicorn
1. To setup the gunicorn go to your project directory in EC2 instance terminal annd make sure that virtual environment is activated

2. Execute this command:
```
gunicorn --workers=3 --bind {APP_HOST_IP_ADDRESS}:{PORT} wsgi:app
```

This specify that we need 3 workers to bind to our app make sure request still processed eventhough there is some worker that are not responding

### Restarting our nginx to start serving our app
1. In the EC2 instance terminal, execute:
```
sudo systemctl restart nginx
```
2. Now our app should be working fine

### Setup elastic IP address
1. EC2 Instance will have different IP address if we shut down the instance and later on start again which we need to re-configure our settings for our app, so we should provisioned one elastic IP address make sure that Public IP address don't change

2. First go to `EC2` console and at the left panel, at the `Network & Security` tab click on `Elastic IPs`

3. Then click on `Allocate Elastic IP Address`

4. Next, choose `us-west-2` for `Network Border Group` and click `Allocate`

5. And click on the newly created elastic IP address and click on `Associate IP Address`

6. Choose `Instance` for `Resource Type`

7. And choose which EC2 instance you want to associate with the elastic IP address and choose the private IP address of your chosen EC2 instance

8. Last, click on `Associate` and we are done allocating elastic IP for EC2

### Update the repository inside EC2 instance terminal
1. To update Github Repository inside the EC2 instance, execute:
```
git pull https://github.com/B10715018/eCloudDay1.git
```

## Documentation
- [How to setup nginx, gunicorn(WGSI) and Django tutorial](https://www.youtube.com/watch?v=I4eN7QQzKd0) 

- [Nginx Documentation](https://nginx.org/en/docs/)

- [Gunicorn Documentation](https://docs.gunicorn.org/en/stable/configure.html)

- [Flask Documentation](https://flask.palletsprojects.com/en/2.1.x/)

# THANK YOU :heart:
