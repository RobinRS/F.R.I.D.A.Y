from datetime import date, timedelta
import time

# Gives you the date of yesterday, today and tomorrow. The keywords (y,t,to) are extracted as entities from wit.ai

def cmd(entities):
    try:
        date_asked = entities['date_specific:date_specific'][0]['body']
    except:
        return "Which day do you want to know?"

    today = date.today()

    if (date_asked == "yesterday"):
        yesterday = date.today() - timedelta(days=1)
        dateYesterday = "Yesterday was the " + str(yesterday.strftime("%d")) + ". " + str(yesterday.strftime("%m")) + ". " + str(yesterday.strftime("%Y")) + "."
        return dateYesterday

    elif (date_asked == "today"):
        dateToday = "Today is the " + str(today.strftime("%d")) + ". " + str(today.strftime("%m")) + ". " + str(today.strftime("%Y")) + "."
        return dateToday

    elif (date_asked == "tomorrow"):
        tomorrow = date.today() + timedelta(days=1)
        dateTomorrow = "Tomorrow we will have the " + str(tomorrow.strftime("%d")) + ". " + str(tomorrow.strftime("%m")) + ". " + str(tomorrow.strftime("%Y")) + "."
        return dateTomorrow
