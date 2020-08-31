# The basic architecture of a function-module: returns a random text

import random

greetings = ["Hello Sir!", "I'm ready", "Good day, Sir!"]

def cmd(entities):
    return random.choice(greetings)
