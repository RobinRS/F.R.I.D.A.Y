## F.R.I.D.A.Y Setup Guide


Here's the guide to setup your own version of the F.R.I.D.A.Y Framework.
For any error, please create a new issue on the GitHub page, or write in the discord server.


### Setup your Wit.ai App
1.	Go to: wit.ai
2.	Create a new Project (you need to login with Facebook) and give it a name: Because of the flexibility of the F.R.I.D.A.Y Framework, because of the flexibility it doesn't matter which name you take, choose one you like!
3.	Also choose the language, which, like the name, does not matter because of the neutral behave of F.R.I.D.A.Y. But it’s recommended to use English because for example when you want to have text to speech output later, English is better supported and the standard functions in here are all in English.
4.	On the left side, click on settings and copy the Server Access Token.
5.	Go to FRIDAY/config.py and paste the Server Access Token to the variable WIT_ACCESS_TOKEN.

### Python-Module requirements
1.	Open your terminal, or anaconda prompt and type in:
###
      pip install -r "YOUR PATH TO\FRIDAY\python_module_requirements.txt"
Make sure, to insert the real path to your FRIDAY directory!

> Try running friday_shell.py. It should work without any errors, but do not do anything.
 
### Create Wit Understandings
1.	Read the Wit.ai Getting Started until 04, for having a better understanding about wit.
2.	Now make your first understanding: 
2.1	Type in the utterance “Hello Friday”.
2.2	Click on the intent box and type in greeting for creating a new intent and click on create intent.
2.3	Click on Train and Validate.
2.4	Do this again with a few other types of saying Hello.
3.	Look at scripts/greeting.py:
###
      from .Function_Module import Function_Module
      import random

      class greeting(Function_Module):
            name = "greeting"
            help_description = "Just saying hello."

            greetings = ["Hello Sir!", "I am ready, Sir", "Good Day, Sir!", "Welcome, Sir!"]

            def respond(self, entities):
                  response = random.choice(self.greetings)

            return response
        
A function_module script must have these components:
###
      from .Function_Module import Function_Module
The class called as the name of the function, (command, intent):
###
      class greeting(Function_Module):
Very important:
#### name: EXACTLY the same name as the name of the intent from wit.ai
help_description: what it does
###
      name = "greeting"
      help_description = "Just saying hello."

And a respond method which returns the output:
###
      def respond(self, entities):
        
This means, that when wit.ai recognizes greeting as the intent, Friday will get the returned answer from the script greeting: FRIDAY\command_executing\scripts\greeting.py, especially the method respond(entities) returns the answer. For more info please read the documentation.
4.	Now run again friday_shell.py and type in “Hello Friday!”. You should now get an answer like “Hello Sir!”
5.	You can add more greetings by adding sentences in the list greetings at the greeting.py script:
  ###
      greetings = ["Hello Sir!", "I am ready", " Good day sir!"]


### Adding the functionality
1.	By looking in the command-executing scripts, you can see, that there are many more commands and functions you can execute by communicate with the F.R.I.D.A.Y Framework. All of these are designed to be executed when a special intent is detected. So, you have to create all these intents in your wit app, with a *specific* name.
2.	For creating a new functionality, create a new intent, give it a very clear name and train it. The create a new script in the scripts folder with the same name as
the intent, with a class with the same name, the name variable ,a respond method and all the other required thing mentioned above. I hardly recommend you to look at the other
scripts in order to understand the logic behind them.
