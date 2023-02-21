import boto3

# standard entry point
def lambda_handler(event, context):
    
    ec2_client = boto3.client('ec2')
    
    # get a list of regions for ec2
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
    
    ### Same as above, easier to read
    # regions = []
    # for region in ec2_client.describe_regions()['Regions']:
    #     regions.append(region['RegionName'])
    ###
    
    for region in regions:
        ec2 = boto3.resouce('ec2', region_name=region)
        print('Region: ', region)
        
        # get only running instances
        instances = ec2.instances.filter(
            Filters = [{'Name': 'instance-state-name',
                        'Values': ['running']}])
        
        # stop the instances 
        for instance in instances:
            instance.stop()
            print('Stopped instance: ', instance.id)