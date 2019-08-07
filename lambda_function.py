import boto3


 # Get list of regions
ec2_client = boto3.client('ec2')
regions = [region['RegionName']
        for region in ec2_client.describe_regions()['Regions']]

# Iterate over each region
for region in regions:
    ec2 = boto3.resource('ec2', region_name=region)

    print("Region:", region)
    # Get only running instances
    ids = []
    instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name',
                    'Values': ['running']}])
    for instance in instances:
        print("Running Instances: ", instance.id)
        ids.append(instance.id)

        if len(ids) >= 1:
            print("Changing tags for %d instances" % len(ids))

            ec2.create_tags(
                Resources=ids,
                Tags=[
                    {
                        'Key': 'Name',
                        'Value': 'Prod-instance'
                    }
                ]
            )
