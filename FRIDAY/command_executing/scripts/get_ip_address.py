from .Function_Module import Function_Module
import socket
import random

class get_ip_address(Function_Module):
    name = "get_ip_address"
    help_description = "My IP Address in the local network"
    IPErrorList = ["I'm sorry, sir, I can't find my IP address.", "Sir, there was an error finding the IP address."]

    def respond(self, entities):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except:
                return random.choice(self.IPErrorList)
        finally:
            s.close()

        returnTextList = ["My IP Address is: " + str(IP), "My IP Address is: " + str(IP)]
        return random.choice(returnTextList)