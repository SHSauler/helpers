#!/usr/bin/env python3

import requests

# Disable insecure warning
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

BASE_URL = ""

def get_url(page):
    
    sleep(STANDOFF_SEC)
    
    url = "{url}/{page}".format(url=BASE_URL,page=page)
    
    try:
        r = requests.get(url)
    except RequestException as e:
        return False
    
    if r.status_code != 200:
        return False
    
    return r.json()
