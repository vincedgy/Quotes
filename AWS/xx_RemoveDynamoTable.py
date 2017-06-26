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
    dynamodb.delete_table(TableName=TABLE_NAME)
    dynamodb.get_waiter('table_not_exists').wait(TableName=TABLE_NAME)
    logger.log('Table '+ TABLE_NAME + ' is now deleted.')    
except ClientError as e:
    raise(e)
    