import os
import time

print("Installing Requirements.....")
try:
    os.system("pip3 install bitcoin")
    time.sleep(2)
    os.system("pip3 install urllib3")
    time.sleep(2)
    os.system("pip3 install fastapi")
    time.sleep(2)
    os.system("pip3 install datetime")
    time.sleep(2)
    os.system("pip3 install uvicorn")
    time.sleep(2)
    os.system("pip3 install requests")
    time.sleep(2)
    os.system("pip3 install psutil")
    time.sleep(2)
    os.system("pip3 install colorama")

except:
    print("No Pip installed!")
