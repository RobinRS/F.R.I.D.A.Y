import random

def cmd(entities):
    answerList = ["Sehr gut!, aber kann es einem Programm eigentlich schlecht gehen?",
    "Gut!, aber habe ich überhaupt Gefühle?",
    "Gut würde ich sagen!", "Ausgezeichnet, Sir und ihnen?",
    "Wie immer bestens Sir, und ihnen?", "Ausgezeichnet!"]
    return random.choice(answerList)