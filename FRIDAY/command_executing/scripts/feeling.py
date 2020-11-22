from .Function_Module import Function_Module
import random

class feeling(Function_Module):
    name = "feeling"
    help_description = "How I feel in the moment."

    def respond(self, entities):
        answerList = ["Very good! But can a program be in a bad way?",
            "Good! But do I have feelings at all?",
            "Good I would say!" , "Excellent, sir and you?",
            "As always good Sir, and you?", "Excellent!"]
        return random.choice(answerList)