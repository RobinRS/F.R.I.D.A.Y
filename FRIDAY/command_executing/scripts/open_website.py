import subprocess
import pathlib
from . import config
import random

answerList = ['Ok, ich öffne ', 'Ich gehe nun auf ']

def open_website(url):
    subprocess.Popen(config.browser_path + " " + url)
    return random.choice(answerList) + " " + url