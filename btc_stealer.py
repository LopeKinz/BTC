from bitcoin import *
import requests
import time
import json
try:    # if is python3
    from urllib.request import urlopen
except: # if is python2
    from urllib2 import urlopen

zero = '[{}]'
l = "null"

version = 1
def server():
    
    count = 1
    while True:
        private_key = random_key()
        public_key = privtopub(private_key)
        address = pubtoaddr(public_key)
        r = requests.get(f"http://127.0.0.1:8000/beta/check/{address}")
        if zero in r.text or l in r.text:
                print(f"Key: {address} | Results : 0")
        else:
                print(f"HIT! Key: {address} | Results : {r.text}")
                with open('wallets.txt', 'a') as the_file:
                    the_file.write(f'{r.text}\n')
                time.sleep(60)



main_menu = '''

    ____ ____________   _____ __             __         
   / __ )_  __/ ____/  / ___// /____  ____ _/ /__  _____
  / __  |/ / / /       \__ \/ __/ _ \/ __ `/ / _ \/ ___/
 / /_/ // / / /___    ___/ / /_/  __/ /_/ / /  __/ /    
/_____//_/  \____/   /____/\__/\___/\__,_/_/\___/_/     
            By Pinkyhax and BanHammer Team
                    PRE RELEASE
            For better experiance use Proxies!                           
'''




error = "Error Checking Key"

online1 = requests.get("http://127.0.0.1:8000/beta/status")
online = online1.text
status1 = "Maintance"
status2 = "Online"

print(main_menu)

verisoncheck = requests.get(f"http://127.0.0.1:8000/version/{version}")

print(verisoncheck.text)

time.sleep(2)

if status1 in online:
    print("Server is under Maintance")
    time.sleep(5)
    exit()
if status2 in online:
    print("Server is Online")
    os.system("cls")
    server()
