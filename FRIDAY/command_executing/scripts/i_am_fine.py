from .Function_Module import Function_Module
import random

class i_am_fine(Function_Module):
    name = "i_am_fine"
    help_description = "When you're fine."

    def respond(intent, entities):
        answerList = ["Nice to heart that!", "Wonderful!", "Great!"]
        return random.choice(answerList)