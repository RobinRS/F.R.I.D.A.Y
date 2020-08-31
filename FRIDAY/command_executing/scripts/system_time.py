from datetime import datetime

def cmd(entities):
    # datetime object containing current date and time
    now = datetime.now()
    system_time = "Es ist " + str(now.strftime("%H")) + " Uhr " + str(now.strftime("%M"))
    return system_time