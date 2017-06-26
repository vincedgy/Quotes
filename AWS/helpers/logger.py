#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Helper module used by all my Python boto scripts """
from __future__ import print_function
import logging

# Ini file
import os
LEVEL=os.getenv('LOGGING_LEVEL', 'INFO')
FILE=os.getenv('LOGGING_FILE', 'logs.log')
print(LEVEL,FILE)

loggingInitialized = False

def initLogging(level='DEBUG', file='logs.log'):
    if file == "NOFILE":
        logging.basicConfig(
            level=level,
            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p',
            )
    else:
        logging.basicConfig(
            level=level,
            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p',
            filename=file,
            filemode='a'
        )     
    loggingInitialized = True
    return loggingInitialized

def log(message='None'):
    if not loggingInitialized:
        initLogging(LEVEL, FILE)
    return logging.info(message)

def error(message='None'):
    if not loggingInitialized:
        initLogging(LEVEL, FILE)
    return logging.error(message)
