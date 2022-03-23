import sys
import re
from time import sleep
from bitcoin import *
try:    # if is python3
    from urllib.request import urlopen
except: # if is python2
    from urllib2 import urlopen
from fastapi import FastAPI, Depends
import random
from datetime import datetime
import json




app = FastAPI()


times = datetime.now()
dt_string = times.strftime("%d/%m/%Y %H:%M:%S")





@app.post('/connected')
def connected(request: Request):
    ip = request.client
    return(f"Connected {ip}")

class status():
    status: str

with open("status.json", "r") as f:
    current_status = json.load(f)['status']

@app.get('/beta/status')
def get_status():
    with open("status.json", "r") as f:
        current_status = json.load(f)['status']
    status = current_status
    return status

@app.get("/version/{version}")
def version(version : int):
    curr_version = 1
    if curr_version > version:
        return("Check for Updates!")
    else:
        return("Lastest Version Installed!")


@app.get('/beta/check/{address}')
def check_balance(address: str):
    

    

 
    WARN_WAIT_TIME = 0

    blockchain_tags_json = [ 
        'final_balance',
        ]

    SATOSHIS_PER_BTC = 1e+8

    check_address = address

    parse_address_structure = re.match(r' *([a-zA-Z1-9]{1,34})', check_address)
    if ( parse_address_structure is not None ):
        check_address = parse_address_structure.group(1)
    else:
        return( "\nThis Bitcoin Address is invalid" + check_address )
        exit(1)

    reading_state=1
    api_requests = 1
    while (reading_state):
        try:
            htmlfile = urlopen("https://blockchain.info/address/%s?format=json" % check_address, timeout = 10 )
            htmltext = htmlfile.read().decode('utf-8')
            reading_state  = 0
            api_requests = api_requests + 1
        except:
            return(f"Error Checking Key | Too many Requests")

            

    blockchain_info_array = []
    tag = ''
    try:
        for tag in blockchain_tags_json:
            blockchain_info_array.append (
                float( re.search( r'%s":(\d+),' % tag, htmltext ).group(1) ) )
    except:
        return( "Error '%s'." % tag )
        exit(1)

    for i, btc_tokens in enumerate(blockchain_info_array):

        sys.stdout.write ("%s \t= " % blockchain_tags_json[i])
        if btc_tokens > 0.0:
            balance = btc_tokens/SATOSHIS_PER_BTC
            return(float(balance))
        else:
            return(0)



