# This is used for the documentation for CI/CD from local to EC2

## How to start ?

- Create `.github` folder and create `{FILE_NAME}.yaml` to deploy to Github Actions

- Insert code as seen in the CI/CD yaml file in the `.github` folder named `deploy.yml`

- Make sure the `AWS_EC2_SSH_KEY` is the right `.pem` file and to extract the file to github secrets this is the right format:
```
-----BEGIN RSA PRIVATE KEY-----
XXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXX
-----END RSA PRIVATE KEY-----  
```

- For `HOSTNAME` would be `ec2-XX-XXX-XXX-XXX.{REGION_NAME}.compute.amazonaws.com`

- For `USERNAME` you should SSH to your VMs and execute to know your username:
```
whoami
```

- `StrictHostKeyChecking=no` in the template yaml ensures that there would be no checking for trusted host or not

- Next, we should change our github remote into SSH instead of HTTPs, to change:
```
git remote set-url origin git@github.com:USERNAME/REPOSITORY.git
```

- verify that it is already change to SSH
```
git remote -v
```

- Now set so that github can SSH to our EC2 instances, first got to our EC2 instance terminal, we need to generate SSH key by, and choose all as default:
```
ssh-keygen -t rsa
```

- Then go to the `.ssh` folder and find file name `id_rsa.pub` it is our public key used to be put into the Github Deploy Key. While `id_rsa` is the EC2 private key which will decode the message encrypted by the public key sent by Github

- Then go to Github, find your repository and go to `Deploy Keys` in `settings` and insert the public key of EC2 instance and don't forget to tick the `Allow Write Access`, format would be:
```
ssh-rsa
XXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXX
```

- Our CI/CD for this project would be ready to go

## To ensure CI/CD works make sure EC2 stays turned on to enable SSH into it !