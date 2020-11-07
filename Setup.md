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
3.	Now look at FRIDAY\command_executing\scripts. You will see, the first if statement:
###
      if (intent == "greeting"):
              from .scripts import greeting
              return greeting.cmd(entities)
This means, that when wit.ai recognizes greeting as the intent, Friday will get the returned answer from the script greeting: FRIDAY\command_executing\scripts\greeting.py, especially the method cmd(entities) returns the answer. For more info please read the documentation.
4.	Now run again friday_shell.py and type in “Hello Friday!”. You should now get an answer like “Hello Sir!”
5.	You can add more greetings by adding sentences in the list greetings at the greeting.py script:
  ###
      greetings = ["Hello Sir!", "I am ready", " Good day sir!"]


### Adding the functionality
1.	By looking in the command-executing scripts, you can see, that there are many more commands and functions you can execute by communicate with the F.R.I.D.A.Y Framework. All of these are designed to be executed when a special intent is detected. So, you have to create all these intents in your wit app, and take the names described in the command-executing script.
2.	For creating a new functionality, create a new intent, give it a very clear name and train it. Then create a new if statement in the command-executing.py and create a new script with the same name. Then in the if-statement, import this script and execute the cmd(entities) method, which takes the entities as parameter. Create this method in your script and return an answer at the end. Orient yourself on the already existing connections of if-statement and script, e.g. the simple greeting script.
