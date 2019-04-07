#!/usr/bin/env python3
import boto3
import time
from ev3dev.ev3 import *

client = boto3.client('sqs')

queue_url = 'https://sqs.eu-west-1.amazonaws.com/229803897151/ev3'

# Define the motors/ports
motor_right = LargeMotor('outA')
motor_left = LargeMotor('outD')

# Check SQS queue every 10 seconds
while True:

    response = client.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )


    try:
    command = response['Messages'][0]
    receipt_handle = command['ReceiptHandle']
        if command['Body'] == 'move_bot_forward':
            print("Moving forward")
            motor_right.run_timed(time_sp=3000, speed_sp=-750)
            motor_left.run_timed(time_sp=3000, speed_sp=-750)
        client.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=receipt_handle
    except:
        print("No messages in SQS")

    time.sleep(10)