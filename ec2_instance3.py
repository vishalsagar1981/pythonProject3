import  boto3

ec2 = boto3.resource("ec2")

for instance in ec2.instances.all():
    print(instance)
    print('Instance Id Is {} and Instance Type Is {}'.format(instance.instance_id, instance.instance_type))
