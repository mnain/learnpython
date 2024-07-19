#!/usr/bin/env python

import sys
import telnetlib
sys.path.append('C:\\users\\mnain\\Documents\\src\\venv\\Lib\\site-packages')
import colorama

def tryTelnet(host, port):
    colorama.init()
    tl = telnetlib.Telnet()
    try:
        telnetHandler = tl.open(host, port, timeout=30)
        print("{}Connected to {}:{}{}".format(colorama.Fore.GREEN,host,port,colorama.Fore.RESET))
        tl.close()
    except TimeoutError:
        print("{}Timeout {}{}".format(colorama.Fore.RED,sys.exc_info()[1],colorama.Fore.RESET))
    except:
        print("{}Could not open telnet session to {}{}{}".format(colorama.Fore.RED,host,port,colorama.Fore.RESET))
        print("{}ERROR: {}{}".format(colorama.Fore.RED,sys.exc_info()[1],colorama.Fore.RESET))

if __name__ == "__main__":
    try:
        host = sys.argv[1]
        port = int(sys.argv[2])
    except:
        print("Telnet: Need arguments: host and port")
        sys.exit()

    tryTelnet(host, port)
