#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" """
from __future__ import print_function
from helpers import logger
import boto3

logger.log("Starting " + __file__ + ":" + __name__)

try:
    client = boto3.client('iam')
except Exception as e:
    logger.error(e)

