from .Function_Module import Function_Module
import random

class personality(Function_Module):
    name = "personality"
    help_description = "Who I am"

    def respond(self, entities):
        answerList = ["I am F.R.I.D.A.Y.", "I am F.R.I.D.A.Y, an artificial intelligence to support you.", "My name is F.R.I.D.A.Y."]
        return random.choice(answerList)