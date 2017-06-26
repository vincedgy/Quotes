# -*- coding: utf-8 -*-
""" """
from __future__ import print_function
from helpers import logger
import json
import boto3
from botocore.exceptions import ClientError

TABLE_NAME='Quotes'

logger.log("Starting " + __file__ + ":" + __name__)

try:  
    dynamodb = boto3.client('dynamodb')
    table = dynamodb.describe_table( TableName=TABLE_NAME )
    pass
except ClientError as e:
    if e.response['Error']['Code'] == 'ResourceNotFoundException':
        logger.log('Creating table ' + TABLE_NAME)
        try:
            dynamodb.create_table(
                TableName=TABLE_NAME,
                KeySchema=[
                    {
                        'AttributeName': 'id',
                        'KeyType': 'HASH'  #Partition key
                    }
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'id',
                        'AttributeType': 'S'
                    },
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 1,
                    'WriteCapacityUnits': 1
                }
            )
            # Wait until the table exists.
            dynamodb.get_waiter('table_exists').wait(TableName=TABLE_NAME)
            table = dynamodb.describe_table( TableName=TABLE_NAME )
            logger.log('Table '+ TABLE_NAME + ' is created.')
        except ClientError as creationError:
            raise(creationError)
else:
    logger.log('Table '+ TABLE_NAME + ' status is ' + table['Table']['TableStatus'])
    print('Table '+ TABLE_NAME + ' ARN is : ' + table['Table']['TableArn'])
    