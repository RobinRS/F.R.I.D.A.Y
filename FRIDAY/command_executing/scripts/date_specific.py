from datetime import date, timedelta
import time

def cmd(entities):
    try:
        date_asked = entities['date_specific:date_specific'][0]['body']
    except:
        return "Welches Datum möchtest du wissen?"

    today = date.today()

    if (date_asked == "gestern"):
        yesterday = date.today() - timedelta(days=1)
        dateYesterday = "Gestern war der " + str(yesterday.strftime("%d")) + ". " + str(yesterday.strftime("%m")) + ". " + str(yesterday.strftime("%Y")) + "."
        return dateYesterday

    elif (date_asked == "heute"):
        dateToday = "Heute ist der " + str(today.strftime("%d")) + ". " + str(today.strftime("%m")) + ". " + str(today.strftime("%Y")) + "."
        return dateToday

    elif (date_asked == "morgen"):
        tomorrow = date.today() + timedelta(days=1)
        dateTomorrow = "Morgen haben wir den " + str(tomorrow.strftime("%d")) + ". " + str(tomorrow.strftime("%m")) + ". " + str(tomorrow.strftime("%Y")) + "."
        return dateTomorrow
