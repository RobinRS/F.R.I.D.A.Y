from .Function_Module import Function_Module
import random

class greeting(Function_Module):
    name = "greeting"
    help_description = "Just saying hello."

    greetings = ["Hello Sir!", "I am ready, Sir", "Good Day, Sir!", "Welcome, Sir!"]

    def respond(self, entities):
        response = random.choice(self.greetings)

        return response