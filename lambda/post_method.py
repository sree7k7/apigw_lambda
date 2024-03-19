import os
import boto3
import json

def lambda_handler(event, context):
    # post method
    print(event)
    return {
        'statusCode': 200,
        'body': json.dumps('hello from post method! ' + event['body'])
    }