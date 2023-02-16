import boto3

s3 = boto3.client('s3')

response = s3.list_objects(Bucket='boto3bucket070622-2')['Contents']

for item in response:
    print(item['Key'])
    
