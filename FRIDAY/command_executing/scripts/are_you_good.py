import random

def cmd(entities):
    answerList = [
        "Yes sir, I'm fine!",
        "Of course sir, I'm in a good mood as always!",
        "I never have bad days.",
        "Can I even feel bad?"
    ]

    return random.choice(answerList)
