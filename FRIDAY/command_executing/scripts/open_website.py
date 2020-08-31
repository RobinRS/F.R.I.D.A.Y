import subprocess
import pathlib
from . import config
import random

answerList = ["Okay, I'm now opening", "I'm now switching to"]

def open_website(url):
    subprocess.Popen(config.browser_path + " " + url)
    return random.choice(answerList) + " " + url
