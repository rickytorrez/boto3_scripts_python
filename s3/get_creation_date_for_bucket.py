import boto3

s3 = boto3.client('s3')

# response = s3.list_buckets()
# buckets = response['Buckets']

# condenses both statements into one
response = s3.list_buckets()['Buckets']

for bucket in response:
    if bucket['Name'] == 'luitlabs':
        print(bucket['CreationDate'])