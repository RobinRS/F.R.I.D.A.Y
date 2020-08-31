import random

def cmd(entities):
    answerList = [
        "Ja Sir, mir geht es bestens!",
        "Natürlich Sir, ich bin wie immer gut gelaunt!",
        "Ich habe nie schlechte Tage.",
        "Kann ich mich überhaupt schlecht fühlen?"
    ]

    return random.choice(answerList)