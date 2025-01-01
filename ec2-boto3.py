import boto3

# Create EC2 resource

#step1

ec2_resource = boto3.resource('ec2')

# step2

instances = ec2_resource.create_instances(
    ImageId = 'ami-053b12d3152c0cc71',
    MinCount = 1,
    MaxCount = 1,
    InstanceType = 't2.micro',
    KeyName = 'ec2boto',
    
    BlockDeviceMappings = [ # If required 
        {
            'DeviceName': '/dev/sda1',
            'Ebs': {
                'VolumeSize': 20,
                'VolumeType': 'gp2',
                'DeleteOnTermination': False
            }
        }
    ],
    TagSpecifications = [
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                'Key': 'Name',
                'Value': 'Myec2boto2',
                },
                {
                'Key':  'Env',
                'Value': 'Test'
                }
            ]
        }
    ],
    # If required
    UserData = '''#!/bin/bash
    #update the package list 
    sudo apt update -y 
    # Install apache
    sudo apt install apache2 -y 
    # start apache service 
    sudo systemctl start apache2
    # enable the service 
    sudo systemctl enable apache2
    # Create sample index.html
    echo "<html><body><h1>Welcome tp Apache web server - Marck</h1></body></html>" | sudo tee /var/www/html/index.html
    # Allow Apache from firewall
    sudo ufw allow 'Apache'
    ''',
)
print('My Instance has been created')
