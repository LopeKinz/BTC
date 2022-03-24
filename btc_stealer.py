from bitcoin import *
import requests
import time
import json
from colorama import Style , Fore , init
try:    # if is python3
    from urllib.request import urlopen
except: # if is python2
    from urllib2 import urlopen
import platform,socket,re,uuid,psutil,logging
from threading import Thread, Lock


zero = '[{}]'
l = "null"
error1 = "Internal"
error2 = "maintance"
hit = "balance"
version = 2

def getSystemInfo():
    try:
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)


def server():
    while True:
        start = time.time()
        private_key = random_key()
        public_key = privtopub(private_key)
        address = pubtoaddr(public_key)
        try:   
            r = requests.get(f"http://127.0.0.1:8000/beta/check/{address}")
        except requests.exceptions.ConnectionError:
            print("API Not Accessable")
            time.sleep(10)
        try:
            if zero in r.text or l in r.text:
                end = time.time()
                print(f"{Fore.YELLOW}PubKey: {address} |PrivKey : {private_key} | Results : 0 |{Fore.MAGENTA} Speed : {end - start} sec")
                
            elif error1 in r.text or error2 in r.text:
                print(f"{Fore.RED}Error #1 NO_API_CONNECTION or Error #2 API_UNDER_MAINTANCE")
                break
                
            elif hit in r.text:
                    print(f"{Fore.GREEN}HIT! PubKey: {address} |PrivKey : {private_key}| Results : {r.text}")
                    with open('wallets.txt', 'a') as the_file:
                        the_file.write(f'{r.text} | {private_key}\n')
                    time.sleep(60)
                    
        except:
                print("Error #3 UNKNOWN ERROR ACCURED!")
                print("-------------------------------")
                print("Send Log to Github Issues Tab! https://github.com/LopeKinz/BTC")
                print("--------------------------------------------------------------")
                print(f"{json.loads(getSystemInfo())}\n"+ r.text)
                break   

main_menu = '''

    ____ ____________   _____ __             __         
   / __ )_  __/ ____/  / ___// /____  ____ _/ /__  _____
  / __  |/ / / /       \__ \/ __/ _ \/ __ `/ / _ \/ ___/
 / /_/ // / / /___    ___/ / /_/  __/ /_/ / /  __/ /    
/_____//_/  \____/   /____/\__/\___/\__,_/_/\___/_/     
            By Pinkyhax and BanHammer Team
                    BETA v2.2                     
'''


print(main_menu)
try:    
    verisoncheck = requests.get(f"http://127.0.0.1:8000/version/{version}")
    online1 = requests.get("http://127.0.0.1:8000/beta/status")
    online = online1.text
    status1 = "Maintance"
    status2 = "Online"
    print(verisoncheck.text)
    time.sleep(2)
    if status1 in online:
        print("Server is under Maintance")
        time.sleep(5)
        exit()
    if status2 in online:
        print("Server is Online")
        os.system("cls")
        threadss = input("Enter the number of threads!: ")
        for _ in range(int(threadss)):
            t = Thread(target=server)
            t.start()
except requests.exceptions.ConnectionError:
    print("API Not Accessable!")
    time.sleep(10)
