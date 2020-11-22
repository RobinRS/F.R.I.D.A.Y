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

#      folder            script            class
from command_executing.command_executing import command_executing


class Friday_Core:

    def __init__(self):
        self.runtime_information = config.RUNTIME_INFORMATION
        self.command_executing = command_executing(self.runtime_information)
        self.access_token = config.WIT_ACCESS_TOKEN

        self.client = Wit(access_token=self.access_token)

    def handle_message(self, response):
        if(self.runtime_information):
            print(response)
            print()

        intents = (response['intents'])
        entities = (response['entities'])
        return self.command_executing.command(intents, entities)


    def friday_core(self, text):
        try:
            return self.handle_message(self.client.message(text))
        except wit.wit.WitError:
            return "Sorry I did not understand you, please check your input! --- Also don't forget to paste your wit access token in config.py"
        except ConnectionError:
            return "Sorry Sir, I think I'm not connected to the internet!"