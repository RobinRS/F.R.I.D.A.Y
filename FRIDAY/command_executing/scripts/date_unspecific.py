# Welches Datum heute


from datetime import date, timedelta
import time

def cmd(entities):
    today = date.today()
    dateToday = "Heute ist der " + str(today.strftime("%d")) + ". " + str(today.strftime("%m")) + ". " + str(today.strftime("%Y")) + "."
    return dateToday