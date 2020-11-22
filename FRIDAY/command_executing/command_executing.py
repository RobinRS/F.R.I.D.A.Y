# -------------------------------------------F.R.I.D.A.Y-------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

# Friday Command_Executing
# Some parts are inspired by: https://github.com/aazuspan/Voithos/blob/master/backend/src/Voithos/CommandHandler.py

import importlib
import pkgutil
import os
from .scripts.Function_Module import Function_Module


class command_executing:

    defaultReturnUnable = "Sorry Sir, I don't understand you."
    noScriptFound = "Sorry Sir, there's no script for this."

    def __init__(self, runtime_information):
        """
        Load (import) all command scripts, Function_Modules when initializing this script (called by friday_core) and not every time with a new command, as this process takes a while
        :param runtime_infos: Getting from the config.py one level up. If true: prints out a lot of information about the execution
        """

        self.runtime_information = runtime_information
        self.command_classes = self.get_commands()
        
        self.printScripts()


    def command(self, intents, entities):
        """
        The method, which is executed in friday_core
        :param intents, entities: The list of intents, entities of the user input (getting from wit)
        :return: returns the answer, reply from the executed command-script
        """

        try:
            intent = intents[0]['name']
        except:
            return self.defaultReturnUnable

        return self.execute_command(intent, entities)


    def execute_command(self,intent, entities):
        """
        Executes the fitting script from the imported ones
        :return: return the response from the executed script
        """
        command_script_to_execute = self.get_cmd_from_name(intent)

        if(command_script_to_execute == None):
            return self.noScriptFound
        else:
            # Der erste Parameter ist immer die Klasse selbst, da die Methode self als Parameter hat: def respond(self, entities)
            return command_script_to_execute.respond(command_script_to_execute, entities)


    def get_cmd_from_name(self, intent):
            """
            Find the command class that matches a given command name
            :param cmd_name: String name of a command
            :return: A command class
            """

            # Every command-script has the attribute name, which is the same as defined in wit.ai
            # Go through each command-class and check if the intent equals the name: Yes, than execute it
            for cmd in self.command_classes:
                if cmd.name == intent:
                    return cmd


    def get_commands(self):
        """
        Find all commands in the command directory and import them. Then return all of them that are subclasses of Command in a list
        :return : A list of classes which are subclasses of Command
        """
        COMMAND_DIR = os.path.join(os.path.dirname(__file__), 'scripts')

        if self.runtime_information: print("Command Directory: ", COMMAND_DIR)

        for (module_loader, name, ispkg) in pkgutil.iter_modules([COMMAND_DIR]):
            importlib.import_module('.scripts.' + name, __package__)
        return Function_Module.__subclasses__()


    def printScripts(self):
        if(self.runtime_information):
            print('\n' + "Detected Function_Modules:")
            # Print detected function_modules
            for cmd in self.command_classes:
                print(cmd.name)