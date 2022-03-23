from bitcoin import *
import requests
import time
import json
try:    # if is python3
    from urllib.request import urlopen
except: # if is python2
    from urllib2 import urlopen

version = 1
def server():
    
    count = 1
    while True:
        private_key = random_key()
        public_key = privtopub(private_key)
        address = pubtoaddr(public_key)
        r = requests.get(f"http://127.0.0.1:8000/beta/check/{address}")
        try:
            if float(r.text) > 0:
                print(f"HIT! Key: {address} | Results : {r.text}")
            else:
                print(f"Key: {address} | Results : {r.text}")
                count = count + 1
                if count > 16:
                    print("Pause against API Abuse!")
                    time.sleep(5)
                    count = 1
                else:
                    pass
        except:
            print(r.text)
            print("Closing...")
            time.sleep(10)
            exit()


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

time.sleep(5)

if status1 in online:
    print("Server is under Maintance")
    time.sleep(5)
    exit()
if status2 in online:
    print("Server is Online")
    time.sleep(5)
    os.system("cls")
    server()
