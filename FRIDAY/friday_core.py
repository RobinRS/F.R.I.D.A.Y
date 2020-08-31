# -------------------------------------------F.R.I.D.A.Y-------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

# Friday Core


import sys
from wit import Wit
import config

import command_executing.command_executing as CE

access_token = config.WIT_ACCESS_TOKEN

client = Wit(access_token=access_token)

def handle_message(response):
    print(response)
    print()

    intents = (response['intents'])
    entities = (response['entities'])
    return CE.command(intents, entities)
    
    print()


def friday_core(text):
    return handle_message(client.message(text))