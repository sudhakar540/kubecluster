#!/usr/bin/env python
import os
import sys
import json
import boto3 

ec2client = boto3.client('ec2',region_name='us-east-1',aws_access_key_id='',aws_secret_access_key='')

response = ec2client.describe_instances(
    Filters=[
        {
	    'Name': 'tag:Name',
            'Values': ['master']
        }
    ]
    )
PublicIpAddress = ""
list= []
instancelist = []
header = "{\'master\': {\'hosts\': "
footer = "},"
for reservation in (response["Reservations"]):
    for instance in reservation["Instances"]:
        PublicIpAddress=instance["PublicIpAddress"]
        list.append(PublicIpAddress);

print header        
print list
print footer
response1 = ec2client.describe_instances(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': ['node']
        }
    ]
    )
PublicIpAddress = ""
list1= []
instancelist = []
header1 = "\'nodes\': {\'hosts\': "
footer1 = "}}"
for reservation in (response1["Reservations"]):
    for instance in reservation["Instances"]:
        PublicIpAddress=instance["PublicIpAddress"]
        list1.append(PublicIpAddress);

print header1
print list1
print footer1

