from .Function_Module import Function_Module
from datetime import date, timedelta
import time

class date_specific(Function_Module):
    name = "date_specific"
    help_description = "The date of yesterday and tomorrow."

    def respond(self, entities):
        try:
            date_asked = entities['date_specific:date_specific'][0]['body']
        except:
            return "Which date do you want to know?"

        today = date.today()

        if (date_asked == "yesterday"):
            yesterday = date.today() - timedelta(days=1)
            dateYesterday = "Yesterday was the " + str(yesterday.strftime("%d")) + ". " + str(yesterday.strftime("%m")) + ". " + str(yesterday.strftime("%Y")) + "."
            return dateYesterday

        elif (date_asked == "today"):
            dateToday = "Heute is the " + str(today.strftime("%d")) + ". " + str(today.strftime("%m")) + ". " + str(today.strftime("%Y")) + "."
            return dateToday

        elif (date_asked == "tomorrow"):
            tomorrow = date.today() + timedelta(days=1)
            dateTomorrow = "Tomorrow is the " + str(tomorrow.strftime("%d")) + ". " + str(tomorrow.strftime("%m")) + ". " + str(tomorrow.strftime("%Y")) + "."
            return dateTomorrow