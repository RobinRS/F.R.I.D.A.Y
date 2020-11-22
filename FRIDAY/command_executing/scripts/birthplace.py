from .Function_Module import Function_Module
import random

class birthplace(Function_Module):
    name = "birthplace"
    help_description = "From where I come"

    def respond(self, entities):
        answerList = ["I'm off a hard drive from a laptop", "I'm from the northern part of the world."]
        return random.choice(answerList)