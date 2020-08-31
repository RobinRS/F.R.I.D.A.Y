# -------------------------------------------F.R.I.D.A.Y-------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

# Friday Command_Executing


defaultReturnUnable = "I'm sorry, Sir, I can't do that yet."
noIntentDetected = "Sorry, this intent isn't described here."

def command(intents, entities):
    try:
        intent = intents[0]['name']
    except:
        return defaultReturnUnable

    if (intent == "greeting"):
        from .scripts import greeting
        return greeting.cmd(entities)

    elif (intent == "personality"):
        from .scripts import personality
        return personality.cmd(entities)

    elif (intent == "birthplace"):
        from .scripts import birthplace
        return birthplace.cmd(entities)

    elif (intent == "date_unspecific"):
        from .scripts import date_unspecific
        return date_unspecific.cmd(entities)

    elif (intent == "date_specific"):
        from .scripts import date_specific
        return date_specific.cmd(entities)

    elif (intent == "system_time"):
        from .scripts import system_time
        return system_time.cmd(entities)

    elif(intent == "get_gps_location"):
        from .scripts import get_gps_location
        return get_gps_location.cmd(entities)

    elif(intent == "get_ip_address"):
        from .scripts import get_ip_address
        return get_ip_address.cmd(entities)

    elif(intent == "feeling"):
        from .scripts import feeling
        return feeling.cmd(entities)

    elif(intent == "are_you_good"):
        from .scripts import are_you_good
        return are_you_good.cmd(entities)

    elif(intent == "you_feel_bad"):
        from .scripts import you_feel_bad
        return you_feel_bad.cmd(entities)

    elif(intent == "open"):
        from .scripts import open
        return open.cmd(entities)
        
    elif(intent == "birthplace"):
        from .scripts import birthplace
        return birthplace.cmd(entities)

    else:
        return noIntentDetected