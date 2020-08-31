import random

def cmd(entities):
    answerList = [
        "Nein Sir, mir geht es gut, danke der Nachfrage.",
        "Eigentlich nicht, gute Laune ist mir nämlich einprogrammiert.",
        "Mir geht es nie schlecht.",
        "Nein, eigentlich fühle ich mich ganz super. Ist bei ihnen auch alles gut?"
    ]

    return random.choice(answerList)