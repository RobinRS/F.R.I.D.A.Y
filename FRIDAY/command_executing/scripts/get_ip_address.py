import socket
import random

IPErrorList = ["Tut mir leid Sir, ich kann meine IP-Adresse leider nicht herausfinden.", "Sir, beim herausfinden der IP ist leider ein Fehler aufgetreten."]

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

    returnTextList = ["Meine IP-Adresse ist: " + str(IP), "Meine IP-Addresse lautet: " + str(IP)]
    return random.choice(returnTextList)