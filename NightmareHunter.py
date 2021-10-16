from pineappledev.pineappledev import *
from getpass import getpass
import os
def nhlogo():
    print("""\x1b[0;31m
\x1b[0;36m ███▄    █  ██▓  ▄████  ██░ ██ ▄▄▄█████▓ ███▄ ▄███▓ ▄▄▄       ██▀███  ▓█████\x1b[0;31m  ██░ ██  █    ██  ███▄    █ ▄▄▄█████▓▓█████  ██▀███  
\x1b[0;36m ██ ▀█   █ ▓██▒ ██▒ ▀█▒▓██░ ██▒▓  ██▒ ▓▒▓██▒▀█▀ ██▒▒████▄    ▓██ ▒ ██▒▓█   ▀\x1b[0;31m ▓██░ ██▒ ██  ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
\x1b[0;36m▓██  ▀█ ██▒▒██▒▒██░▄▄▄░▒██▀▀██░▒ ▓██░ ▒░▓██    ▓██░▒██  ▀█▄  ▓██ ░▄█ ▒▒███  \x1b[0;31m ▒██▀▀██░▓██  ▒██░▓██  ▀█ ██▒▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
\x1b[0;36m▓██▒  ▐▌██▒░██░░▓█  ██▓░▓█ ░██ ░ ▓██▓ ░ ▒██    ▒██ ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄\x1b[0;31m ░▓█ ░██ ▓▓█  ░██░▓██▒  ▐▌██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  
\x1b[0;36m▒██░   ▓██░░██░░▒▓███▀▒░▓█▒░██▓  ▒██▒ ░ ▒██▒   ░██▒ ▓█   ▓██▒░██▓ ▒██▒░▒████\x1b[0;31m▒░▓█▒░██▓▒▒█████▓ ▒██░   ▓██░  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
\x1b[0;36m░ ▒░   ▒ ▒ ░▓   ░▒   ▒  ▒ ░░▒░▒  ▒ ░░   ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░ ▒ \x1b[0;31m ░░▒░▒░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒   ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
\x1b[0;36m░ ░░   ░ ▒░ ▒ ░  ░   ░  ▒ ░▒░ ░    ░    ░  ░      ░  ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░ ▒ ░\x1b[0;31m▒░ ░░░▒░ ░ ░ ░ ░░   ░ ▒░    ░     ░ ░  ░  ░▒ ░ ▒░
\x1b[0;36m   ░   ░ ░  ▒ ░░ ░   ░  ░  ░░ ░  ░      ░      ░     ░   ▒     ░░   ░    ░    ░  ░░\x1b[0;31m ░ ░░░ ░ ░    ░   ░ ░   ░         ░     ░░   ░ 
\x1b[0;36m         ░  ░        ░  ░  ░  ░                ░         ░  ░   ░        ░  ░ ░  ░  ░\x1b[0;31m   ░              ░             ░  ░   ░     
    \x1b[0;31m
#################################################################
                            \x1b[0;34mBy x04000
                    \x1b[0;33mGithub: github.com/x04000
                    \x1b[0;32mBase: Python, PineappleDev
                          \x1b[0;36mVersion: 0.2
\x1b[0;31m#################################################################
\x1b[0;35m
    """)
def nhclear():
    try:
        os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    except:
        print("")
nhclear()
nhlogo()
def nhinst():
    try:
        while(True):
            print("\x1b[1;36m┌──(\x1b[1;31mroot@\x1b[1;0mNightmareHunter\x1b[1;36m)-\x1b[1;36m[\x1b[1;0m~\x1b[1;36m]")
            nhinst = str(input("\x1b[1;36m└─$ \x1b[0;31m"))
            if nhinst == "exit":
                nhclear()
                nhlogo()
                break
            if nhinst == "clear":
                nhclear()
            if nhinst == "autoinst":
                try:
                    if os.path.isdir("PineappleKiller"):
                        print("\x1b[1;31mYou have got installed: PineappleKiller !")
                    else:
                        os.system("sudo apt-get install git")
                        os.system("git clone https://github.com/x04000/PineappleKiller")
                    if os.path.isdir("Meatballs"):
                        print("\x1b[1;31mYou have got installed: Meatballs !")
                    else:
                        os.system("sudo apt-get install git")
                        os.system("git clone https://github.com/SkyWtkh/Meatballs")
                except:
                    print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
            if nhinst == "update":
                try:
                    os.system("sudo apt-get install git")
                    if os.path.isdir("PineappleKiller"):
                        os.system("sudo rm -rfv PineappleKiller")
                    os.system("git clone https://github.com/x04000/PineappleKiller")
                    if os.path.isdir("Meatballs"):
                        os.system("sudo rm -rfv Meatballs")
                    os.system("git clone https://github.com/SkyWtkh/Meatballs")
                except:
                    print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
            if nhinst == "inst PineappleKiller":
                if os.path.isdir("PineappleKiller"):
                    print("\x1b[1;31mYou have got installed: PineappleKiller !")
                else:
                    os.system("sudo apt-get install git")
                    os.system("git clone https://github.com/x04000/PineappleKiller")
            if nhinst == "update PineappleKiller":
                if os.path.isdir("PineappleKiller"):
                    os.system("sudo apt-get install git")
                    os.system("sudo rm -rfv PineappleKiller")
                    os.system("git clone https://github.com/x04000/PineappleKiller")
                else:
                    print("You haven't got installed: PineappleKiller !")
            if nhinst == "remove PineappleKiller":
                if os.path.isdir("PineappleKiller"):
                    os.system("sudo rm -rfv PineappleKiller")
                else:
                    print("\x1b[1;31mYou haven't got installed: PineappleKiller !")
            if nhinst == "inst mtblls":
                if os.path.isdir("Meatballs"):
                    print("\x1b[1;31mYou have got installed: Meatballs!")
                else:
                    os.system("sudo apt-get install git")
                    os.system("git clone https://github.com/SkyWtkh/Meatballs")
            if nhinst == "update mtblls":
                if os.path.isdir("Meatballs"):
                    os.system("sudo apt-get install git")
                    os.system("sudo rm -rfv Meatballs")
                    os.system("git clone https://github.com/SkyWtkh/Meatballs")
                else:
                    print("You haven't got installed: Meatballs !")
            if nhinst == "remove mtblls":
                if os.path.isdir("Meatballs"):
                    os.system("sudo rm -rfv Meatballs")
                else:
                    print("\x1b[1;31mYou haven't got installed: Meatballs !")
    except:
        print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
try:
    while(True):
        print("\x1b[1;36m┌──(\x1b[1;31mHunter💀NightmareHunter\x1b[1;36m)-\x1b[1;36m[\x1b[1;0m~/NightmareHunter\x1b[1;36m]")
        nhi = str(input("\x1b[1;36m└─$ \x1b[0;31m"))
        if nhi == "exit":
            print("\x1b[1;32mHave a good day :)")
            break
        elif nhi == "clear":
            nhclear()
        elif nhi == "nhlogo":
            nhlogo()
        elif nhi == "nhinst":
            nhclear()
            nhlogo()
            nhinst()
        elif nhi == "PineappleKiller":
            if os.path.isdir("PineappleKiller"):
                try:
                    os.system("cd PineappleKiller && python3 PineappleKiller.py && cd ..")
                except:
                    print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
            else:
                print("\x1b[1;31mYou haven't got installed: PineappleKiller !")
        elif nhi == "mtblls":
            if os.path.isdir("Meatballs"):
                try:
                    os.system("cd Meatballs && python3 AdvancedMeatballs.py && cd ..")
                except:
                    print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
            else:
                print("\x1b[1;31mYou haven't got installed: AdvancedMeatballs !")
        elif nhi == "filemodifiergui":
            p_filemodifiergui()
        elif nhi == "cfile":
            nhfilename = str(input("\x1b[0;31mNightmareHunter > Filename \x1b[0;36m#\x1b[0;32m "))
            p_CFILE(nhfilename)
        elif nhi == "delfile":
            nhfilename = str(input("\x1b[0;31mNightmareHunter > Filename \x1b[0;36m#\x1b[0;32m "))
            p_DELFILE(nhfilename)
        elif nhi == "rfile":
            nhfilename = str(input("\x1b[0;31mNightmareHunter > Filename \x1b[0;36m#\x1b[0;32m "))
            p_RFILE(nhfilename)
        elif nhi == "wfile":
            nhfilename = str(input("\x1b[0;31mNightmareHunter > Filename \x1b[0;36m#\x1b[0;32m "))
            nhwrite= str(input("\x1b[0;31mNightmareHunter > Write \x1b[0;36m#\x1b[0;32m "))
            p_WFILE(nhfilename, nhwrite)
        elif nhi == "gitclone":
            try:
                os.system("sudo apt-get install git")
            except:
                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
            try:
                nhgitclone = str(input("\x1b[0;31mNightmareHunter > URL \x1b[0;36m#\x1b[0;32m "))
                p_gitclone(nhgitclone)
            except:
                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
        elif nhi == "pipinstall":
            try:
                nhpipinst = str(input("\x1b[0;31mNightmareHunter > Package \x1b[0;36m#\x1b[0;32m "))
                p_pipinstall(nhpipinst)
            except:
                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
        elif nhi == "pipuninstall":
            try:
                nhpipuninst = str(input("\x1b[0;31mNightmareHunter > Package \x1b[0;36m#\x1b[0;32m "))
                p_pipuninstall(nhpipuninst)
            except:
                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
        elif nhi == "piplist":
            try:
                p_piplist()
            except:
                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
        elif nhi == "ep":
            try:
                nhep = str(input("NightmareHunter > EP # "))
                p_ep(nhep)
            except:
                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
        elif nhi == "use.login":
            try:
                nhpdusername = str(input("\x1b[0;31mNightmareHunter > Username \x1b[0;36m#\x1b[0;32m "))
                nhpdpassword = getpass("\x1b[0;31mNightmareHunter > Package \x1b[0;36m#\x1b[0;32m ")
                p_login(nhpdusername, nhpdpassword)
            except:
                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
        elif nhi == "use.logingui":
            try:
                nhpdusername = str(input("\x1b[0;31mNightmareHunter > Username \x1b[0;36m#\x1b[0;32m "))
                nhpdpassword = getpass("\x1b[0;31mNightmareHunter > Package \x1b[0;36m#\x1b[0;32m ")
                p_logingui(nhpdusername, nhpdpassword)
            except:
                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
        elif nhi == "use.pin":
            try:
                nhpdpin = getpass("\x1b[0;31mNightmareHunter > Pin \x1b[0;36m#\x1b[0;32m ")
                p_pin_noint(nhpdpin)
            except:
                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
        elif nhi == "use.pingui":
            try:
                nhpdpin = getpass("\x1b[0;31mNightmareHunter > Pin \x1b[0;36m#\x1b[0;32m ")
                p_pingui(nhpdpin)
            except:
                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
        else:
            try:
                os.system(nhi)
            except:
                print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")
except:
    print("\n\x1b[0;31m[\x1b[0;36m!\x1b[0;31m] Keyboard interrupt")