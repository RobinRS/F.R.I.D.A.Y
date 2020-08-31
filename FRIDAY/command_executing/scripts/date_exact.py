from datetime import date, timedelta
import time
from calendar import monthrange


def get_days_in_a_month(date):
    return monthrange(date.year, date.month)[1]

def cmd(entities):
    #try:
    deltaTime = entities['deltaTime:deltaTime'][0]['body']
    timespan = entities['timespan:timespan'][0]['body']
    if(len(entities['time_type:time_type']) == 2):
        time_type = entities['time_type:time_type'][1]['body']      # Wichtig: Das 2 Element denn: Welcher Tag in 2 Jahren: Tag erkennt er als time_type
    else:
        time_type = entities['time_type:time_type'][0]['body']
    #except:
    #return "Welches Datum möchtest du wissen?"

    today = date.today()

    # Zeitspanne = vor (Vergangenheit)
    if(timespan == "vor"):

        # Tage
        if(time_type=="tagen" or time_type=="Tagen" or time_type=="tage" or time_type=="Tage"or time_type=="Tag" or time_type=="tag"):
            date_searched = today - timedelta(days=int(deltaTime))

        # Monate
        elif(time_type=="monaten" or time_type=="Monaten" or time_type=="monate" or time_type=="Monate"):
            date_searched = today - timedelta(days=(int(deltaTime)*get_days_in_a_month(today)))     # Umrechung von Monat in Tage, mithifle von wieviele Tage der Monat hat

        # Jahre
        elif(time_type=="jahren" or time_type=="Jahren" or time_type=="jahre" or time_type=="Jahre"):
            date_searched = today - timedelta(days=(int(deltaTime)*365))    # Umrechnung von Jahr in Tage

    # Zeitspanne = in (Zukunft)
    if(timespan == "in"):
        # Tage
        if(time_type=="tagen" or time_type=="Tagen" or time_type=="tage" or time_type=="Tage" or time_type=="Tag" or time_type=="tag"):
            print("In tagen")
            date_searched = today + timedelta(days=int(deltaTime))

        # Monate
        elif(time_type=="monaten" or time_type=="Monaten" or time_type=="monate" or time_type=="Monate"):
            print("In Monaten")
            date_searched = today + timedelta(days=(int(deltaTime)*get_days_in_a_month(today)))     # Umrechung von Monat in Tage, mithifle von wieviele Tage der Monat hat

        # Jahre
        elif(time_type=="jahren" or time_type=="Jahren" or time_type=="jahre" or time_type=="Jahre"):
            print("In Jahren")
            date_searched = today + timedelta(days=(int(deltaTime)*365))    # Umrechnung von Jahr in Tage

    try:
        return date_searched
    except:
        return "Welches Datum möchtest du wissen?"