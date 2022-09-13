import boto3

client = boto3.client("ec2")

response = client.terminate_instances(InstanceIds = ['i-0af2f8b31eeca7456','i-0f331cf8bf10c6546'])

for instance in response['TerminatingInstances']:
    print('The Instance with Id {} terminated'.format(instance['InstanceId']))