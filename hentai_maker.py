#################################
#  Made by ravi0li / ch0colate  #
#  So yeah, fuck you if ur not  #
#  allowed to be here.          #
#################################

import os, requests
from colorama import Fore, Style
# from lxml.html import fromstring
# from bs4 import BeautifulSoup

#############EDIT ME#############
operative_system = "win"        #  << Put here win or lin
#################################

def banner():
    if operative_system == "win":
        os.system("cls")
    elif operative_system == "lin":
        os.system("clear")
    else:
        print()
        print(" %s%s[!] Error. Invalid operative system, exiting...%s" % (Style.BRIGHT, Fore.RED, Style.RESET_ALL))
        print()

    print()
    print(" %s%s  ::   .: .,:::::::::.    :::.:::::::::::::::.     :::" % (Style.BRIGHT, Fore.WHITE))
    print("  ,;;   ;;,;;;;''''`;;;;,  `;;;;;;;;;;;'''';;`;;    ;;;  dynasty-scans.com")
    print(" ,[[[,,,[[[ [[cccc   [[[[[. '[[     [[    ,[[ '[[,  [[[  DOWNLOADER")
    print(" \"$$$\"\"\"$$$ $$\"\"\"\"   $$$ \"Y$c$$     $$   c$$$cc$$$c $$$  MADE BY")
    print("  888   \"88o888oo,__ 888    Y88     88,   888   888,888  @ravi0li / @ch0colate")
    print("  MMM    YMM\"\"\"\"YUMMMMMM     YM     MMM   YMM   \"\"` MMM%s" % Style.RESET_ALL)
    print()

try:
    banner()
    print(" %s%s[i] %sExample: %s\"/system/releases/000/028/328/\"" % (Style.BRIGHT, Fore.BLUE, Fore.WHITE, Style.RESET_ALL))
    URL = input(" %s%s[i] Type the manga url like in the example %s>> %s" % (Style.BRIGHT, Fore.BLUE, Fore.WHITE, Style.RESET_ALL))
    print()
except KeyboardInterrupt:
    print(" Detected Ctrl+C. Shutting down...%s" % Style.RESET_ALL)
    print()
    exit(1)

if URL[-1] == "/":
    URL = URL[:-1].strip()

if "/" not in URL:
    print(" %s%s[!] Error. Invalid URL input, exiting...%s" % (Style.BRIGHT, Fore.RED, Style.RESET_ALL))
    print()
    exit(1)
if "#" in URL:
    image_format = True
    complex = True
    str_len = int(URL.split("/")[-1].split("#")[1].split(".")[0])
    if "jpg" in URL:
        image_type = ".jpg"
    elif "png" in URL:
        image_type = ".png"
elif "jpg" or "png" in URL.split("/")[-1]:
    image_format = True
    complex = False
    str_len = int(len(URL.split("/")[-1].split(".")[0]))
    if "jpg" in URL:
        image_type = ".jpg"
    elif "png" in URL:
        image_type = ".png"
elif "jpg" or "png" not in URL.split("/")[-1]:
    image_format = False
    image_type = ".jpg"
    URL = URL + "/"
    str_len = 4

try:
    number2fill = 0
    if operative_system == "win":
        os.system("if exist \"u_temp\" rmdir/q/s u_temp")
        os.system("if not exist \"u_temp\" mkdir u_temp")
    elif operative_system == "lin":
        os.system("rm -r u_temp")
        os.system("mkdir u_temp")
    else:
        print()
        print(" %s%s[!] Error. Invalid operative system, exiting...%s" % (Style.BRIGHT, Fore.RED, Style.RESET_ALL))
        print()
    while True:
        number2fill = int(number2fill) + 1
        number = str(number2fill).zfill(str_len)
        if not image_format:
            THIS_IMG = "https://dynasty-scans.com" + URL + number + ".jpg"
        elif image_format:
            if complex:
                THIS_IMG = "https://dynasty-scans.com" + "/".join(URL.split("/")[:-1]) + "/" + URL.split("/")[-1].split("#")[0] + number + image_type
            elif not complex:
                THIS_IMG = "https://dynasty-scans.com" + "/".join(URL.split("/")[:-1]) + "/" + number + image_type
        ## DEBUG ##
        # print(THIS_IMG)
        # input()
        # exit(1)
        try:
            r = requests.get(THIS_IMG, allow_redirects=True)
            images = {"image/jpeg", "image/png"}
            if r.headers["content-type"] not in images:
                print()
                if operative_system == "win":
                    input(" %s%s[+]%s All done! Press enter to exit...%s" % (Style.BRIGHT, Fore.GREEN, Fore.WHITE, Style.RESET_ALL))
                else:
                    print(" %s%s[+]%s All done! Exiting...%s" % (Style.BRIGHT, Fore.GREEN, Fore.WHITE, Style.RESET_ALL))
                exit(1)
            os.system("echo.> u_temp/" + number + image_type)
            PATH = "u_temp/" + number + image_type
            open(str(PATH), "wb").write(r.content)
            print(f" [{Style.BRIGHT}{Fore.GREEN}-{Fore.WHITE}] {Style.RESET_ALL}{Style.DIM}{Fore.WHITE}" + THIS_IMG + f"{Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE} downloaded!")
        except Exception as e:
            print(" %s%s[!] An error ocurred: %s%s" % (Style.BRIGHT, Fore.RED, Style.RESET_ALL, e))
            print()
            exit(1)
except KeyboardInterrupt:
    print(" Detected Ctrl+C. Shutting down...%s" % Style.RESET_ALL)
    print()
    exit(1)

exit(1)
