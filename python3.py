#!/usr/bin/env python3

"""
App docstring

"""

# Standard imports
import uuid
import logging
import sys
import json

# disabling HTTPS unverified errors
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# External imports
import krautsalat

__author__ = "Steffen Sauler"
__email__ = "steffen.sauler@"

############################## Settings #######################################



############################## /Settings ######################################

if sys.version_info[0] < 3:
    raise Exception("This module requires Python 3.0+")

# UUID of run
run_uuid = uuid.uuid4().hex

# Logging
logger = logging.getLogger(__name__)

if DEBUG == True:
    log_filehandle = logging.StreamHandler(sys.stdout)
else:
    log_filehandle = logging.FileHandler(LOGFILE)

uuid = {"uuid" : run_uuid[:6]}
formatter = logging.Formatter('[%(asctime)s]{%(pathname)s:%(lineno)4d}-%(uuid)s-'
                              '%(levelname)s-%(message)s', '%y-%m-%d %H:%M:%S')
log_filehandle.setFormatter(formatter)
logger.addHandler(log_filehandle)
logger.setLevel(LOGLEVEL)
logger = logging.LoggerAdapter(logger, uuid)
logger.info("Started run of {0}".format(run_uuid))

def arguments_parsing():
    """Getting arguments"""
    
    parser = argparse.ArgumentParser(description='description')
    parser.add_argument("-c", "--category", type=str, metavar="CATEGORY",
                        dest="misp_category",  
                        help="Category of MISP attribute to export")
    parser.add_argument("-f", "--filename", type=str, metavar="FILE",
                        action="store", dest="filename",
                        help="Name of file")
    parser.add_argument("-j", "--json", action="store_true",
                        help="Use JSON-File instead of command line")
    args = parser.parse_args()
    return args

def main():
    """ Main function """
    args = arguments_parsing()
    
    # do stuff

if __name__ == "__main__":
    main()
