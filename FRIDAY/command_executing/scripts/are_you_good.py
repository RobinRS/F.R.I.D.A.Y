from .Function_Module import Function_Module
import random

class are_you_good(Function_Module):
    name = "are_you_good"
    help_description = "If I'm fine."

    def respond(self, entities):
        answerList = [
            "Yes sir, I'm fine!",
            "Of course sir, I'm in a good mood as always!",
            "I never have bad days.",
            "Can I even feel bad?"
            ]
        return random.choice(answerList)