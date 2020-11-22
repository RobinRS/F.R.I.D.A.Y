import subprocess
import pathlib
from . import config
import random

answerList = ["Okay, I'm now opening", "I'm now switching to"]

def open_website(url):
    try:
        subprocess.Popen(config.browser_path + " " + url)
    except FileNotFoundError:
        return "Sir, there's a wrong browser path in scripts/config.py!"
    return random.choice(answerList) + " " + url
