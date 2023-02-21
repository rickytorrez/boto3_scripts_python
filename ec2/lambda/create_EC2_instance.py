# os allows us to access our environment variable
import os
# boto3 is aws sdk for python
import boto3

# global variables

# aws machine image we use to provision the ec2 instance
AMI = os.environ['AMI']
# instance type for the virtual machine
INSTANCE_TYPE = os.environ['INSTANCE_TYPE']
# key pair name
KEY_NAME = os.environ['KEY_NAME']
# public subnet that will allow us to ssh into the instance
SUBNET_ID = os.environ['SUBNET_ID']

# ec2 boto3 resource creation
ec2 = boto3.resource('ec2')

# defines lambda entry point
def lambda_handler(event, context):
    
    # global variables are passed to the create_instances function
    instance = ec2.create_instances(
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SubnetId=SUBNET_ID,
        MaxCount=1,
        MinCount=1
    )

    # prints the id of the instance created
    print("New instance created:", instance[0].id)
    
# This lambda function will need the following env variables to function
# AMI, INSTANCE_TYPE, KEY_NAME & SUBNET_ID
# A security group is also needed to be able to SSH into this created instance