# -------------------------------------------F.R.I.D.A.Y-------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

# Friday Core


import sys
import wit
from wit import Wit
import config

import command_executing.command_executing as CE

access_token = config.WIT_ACCESS_TOKEN

client = Wit(access_token=access_token)

def handle_message(response):
    if(config.PRINT_WIT_INFO):
        print(response)
        print()

    intents = (response['intents'])
    entities = (response['entities'])
    return CE.command(intents, entities)


def friday_core(text):
    try:
        return handle_message(client.message(text))
    except wit.wit.WitError:
        return "Sorry, I did not understand you."