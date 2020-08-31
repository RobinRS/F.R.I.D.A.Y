# For executing the command in cmd
import subprocess

import sys

# Random answers
import random
# For finding the path of this script
import pathlib


answerSuccessList = ["Ok, I'm now opening", "Ok, I'm now starting"]
unableFindProgramAnswers = ["Sir, I can't find this program", "Sir, I'm unable to find this program."]


def parseConfFile(textFile):
    pathDict = {}

    for line in textFile:
        
        parsedText = str(line).split(" & ")
        keyword = parsedText[0]
        path = parsedText[1]

        # Add the new pair to the dictionary so that they can then be queried
        pathDict[keyword] = path

    return pathDict


def open_program(program):
    # Lower all letters of the program entered by the user in order to improve the matching
    program = program.lower()

    # Open the file that contains the paths based on the keywords in read mode
    try:
        # The file is in the same directory, i.e. the directory of this script (pathlib)
        textFile = open(str( pathlib.Path(__file__).parent.absolute() ) + r"\program_list.txt", "r")
    except:
        print("Ich finde die Konfigurations-Datei nicht!")
        sys.exit(0)

    # Get the pair keyword-program_path out of the conf_file (program_list.txt)
    pathDict = parseConfFile(textFile)


    try:
        # Get the path from the dictionary based on the keyword from the client
        path = pathDict[program]

        # Important: When parsing, a new line is added to all of them (except for the last element, therefore if not); it is deleted here
        if not (program == list(pathDict)[-1]):
            path = path[:-1]

        subprocess.Popen(path)

        textFile.close()

        return random.choice(answerSuccessList) + " " + program

    # If the program isn't declared in the program_list.txt
    except KeyError:
        return random.choice(unableFindProgramAnswers)
