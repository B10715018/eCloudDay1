# This is the documentation for docker, ECR and ECS

## Containerized the application using Docker
- For the docker make sure that you have Docker installed on your local machine

- Make sure that you create your [Dockerfile](../Dockerfile) in your root repository

- To wrap your app into a container execute: 
```
docker build -t {name_of_container} .
```

For mac m1 chip image will be built in different architecture which is not compatible with the ECS when being deploy
Instead you should execute this command:
```
 docker build --platform linux/amd64 -t {name_of_container} .
 ```

- After building a container we should try to run the container make sure it run as expected
 ```
 docker run -d -p {APP_PORT}:{LOCAL_MACHINE_PORT} {CONTAINER_NAME}
 ```

## Push Container to ECR registry

 - Create the ECR Registry in AWS Console and Create the repository

- Tag your docker image :
 ```
 docker tag {YOUR_CONTAINER_NAME} {YOUR_IMAGE_URI}
 ```

- Configure your AWS profile in CLI ( Enter AWS Access Key and ID):
 ```
 aws configure
 ```

- Pipe the token from ECR to our Docker in order to enable to push container to the ECR
 ```
 aws ecr get-login-password --region {REGION_NAME} | docker login --username AWS --password-stdin [your account number].dkr.ecr.[REGION_NAME].amazonaws.com
 ```

- Push your docker image to ECR
 ```
 docker push {IMAGE_URI}
 ```

- Make sure that your container is uploaded to ECR , check to the AWS console

 ## Create Fargate Cluster

 - Search for `Elastic Container Service` in AWS Console

 - Choose `Cluster` in the left navigation panel

 - Select `Create Cluster`

 - Choose `Networking Only` for the Cluster Template as we will be using AWS Fargate

 - Give name for your AWS Fargate Cluster

 - Tick the `Create VPC` and Click `Create`

 ## Create ECS Task

 - Select `Task Definitions` on the left navigation panel in the AWS Console

 - Select `Fargate` and select `Next Step`

 - Enter the name for your task

 - Leave `Task Role` and `Network Mode` set to their default values

 - Leave `Task Execution Role` to be default

 - For Task Memory and Task CPU set it to 1GB and 0.5 vCPU

 - Under the container definition select `Add Container`

 - Insert desired name for container in `Container Name` and {YOUR_IMAGE_URI} in `Image`

 - Set the `Memory limit` to 128 MiB

 - Set the `Port Mappings` to your target port to the container

 - Leave everything left as default and click `Add`

 - Finally click `Create` and make sure that Task Definition is active

 ##  Set the IAM Role

 - First of all make sure to create policy for the role that would be use later inside the container

 -  The policy should be like this :
 ```
 {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "states:ListStateMachines",
                "ec2:DescribeInstances",
                "states:DescribeStateMachine",
                "wafv2:GetWebACLForResource",
                "dynamodb:ListTables",
                "logs:DescribeLogStreams",
                "cognito-identity:ListIdentityPools",
                "sns:ListTopics",
                "wafv2:GetWebACL",
                "s3:ListBucket",
                "s3:GetBucketPolicy",
                "ec2:DescribeInternetGateways",
                "elasticloadbalancing:DescribeLoadBalancers",
                "logs:CreateLogStream",
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribeAvailabilityZones",
                "dynamodb:DescribeTable",
                "logs:GetLogEvents",
                "rds:DescribeDBInstances",
                "apigateway:GET",
                "ec2:DescribeNetworkAcls",
                "ec2:DescribeRouteTables",
                "wafv2:ListResourcesForWebACL",
                "cognito-identity:DescribeIdentityPool",
                "s3:GetBucketPublicAccessBlock",
                "cloudtrail:LookupEvents",
                "sqs:ListQueues",
                "sns:GetTopicAttributes",
                "lambda:ListFunctions",
                "logs:DescribeLogGroups",
                "dynamodb:PutItem",
                "ecr:GetAuthorizationToken",
                "dynamodb:Scan",
                "sqs:GetQueueAttributes",
                "ec2:DescribeSecurityGroups",
                "s3:PutObject",
                "s3:ListAllMyBuckets",
                "elasticloadbalancing:DescribeTargetHealth",
                "elasticloadbalancing:DescribeTargetGroups",
                "ec2:DescribeVpcEndpoints",
                "ec2:DescribeSubnets",
                "lambda:GetPolicy"
            ],
            "Resource": "*"
        }
    ]
}
 ```

 -  Then create your own role and choose the role for `AWS Service` with particular choice which is `AWS Elastic Container Service Task`

 -  Don't forget to add the policy for `Add Permission` in the IAM Role and click `Create`

 ## Run the ECS Task

 -  Select Task in the `Task Definition` lists

 - Click `Actions` and click `Run Tasks`

 - For `Launch Type` select `Fargate`

 - Make sure `Cluster` is the cluster name that we make previously

 - Choose the Cluster VPC that we previously made

 - Choose all the Public Subnet and make sure `Auto-assign Public IP` is enabled

 - Edit the `Security Group`, make sure that you have Inbound Rule for HTTP and add `Custom TCP` and the `Port` would be where you hosted the app port

 - Make sure that `ECS Managed Tags` is unticked

 - Last open the Advanced Options and For the `Task Overrides` add your own role that we created previously

 - Last click `Run Task` and make sure task is running perfectly using the Public IP of the ECS Task

 # Thank You :))