import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_vpcs()['Vpcs']

# number of VPCs
print(len(response))

# VPC Ids for your account
for vpc in response:
    print(vpc['VpcId'])
    