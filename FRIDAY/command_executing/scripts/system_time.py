from .Function_Module import Function_Module
from datetime import datetime

class system_time(Function_Module):
    name = "system_time"
    help_description = "What time it is"

    def respond(self, entities):
        # datetime object containing current date and time
        now = datetime.now()
        system_time = "It's " + str(now.strftime("%H")) + ":" + str(now.strftime("%M"))
        return system_time