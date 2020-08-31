from datetime import datetime

def cmd(entities):
    # datetime object containing current date and time
    now = datetime.now()
    system_time = "It's " + str(now.strftime("%H")) + ":" + str(now.strftime("%M"))
    return system_time
