import socket
import random

IPErrorList = ["Sorry Sir, I can't find my IP address.", "Sir, there was an error trying to find the IP."]

def cmd(entities):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
            return random.choice(IPError)
    finally:
        s.close()

    returnTextList = ["My IP-Address is: " + str(IP)]
    return random.choice(returnTextList)
