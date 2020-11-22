from .Function_Module import Function_Module
from datetime import date, timedelta
import time

class date_unspecific(Function_Module):
    name = "date_unspecific"
    help_description = "What day is today"

    def respond(self, entities):
        today = date.today()
        dateToday = "Today is the " + str(today.strftime("%d")) + ". " + str(today.strftime("%m")) + ". " + str(today.strftime("%Y")) + "."
        return dateToday