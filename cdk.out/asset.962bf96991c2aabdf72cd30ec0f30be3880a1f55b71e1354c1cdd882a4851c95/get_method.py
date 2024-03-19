import os
import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('This is get method from Lambda!')
    }