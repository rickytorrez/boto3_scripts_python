import boto3

s3 = boto3.client('s3')

response = s3.upload_file(
    Filename='upload.png', # name of file being uploaded
    Bucket='luitlabs',
    Key='uploadtest.png') # name of file once ince the bucket

print(response)