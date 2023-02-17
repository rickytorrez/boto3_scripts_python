import boto3

ec2 = boto3.client('ec2')

response = ec2.delete_vpc(
    VpcId='vpc-0e513cbb6da65b4e7'
    )

print(response)