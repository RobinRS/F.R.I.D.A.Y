import random

def cmd(entities):
    answerList = [
        "No sir, I'm fine, thanks for asking.",
        "Not really, because I'm in a good mood ..",
        "I never feel bad.",
        "No, actually I feel really great. Is everything okay with you too?",
        "No, I'm programmed to be happy!"
    ]

    return random.choice(answerList)
