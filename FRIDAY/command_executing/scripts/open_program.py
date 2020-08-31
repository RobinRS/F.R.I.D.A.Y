# Zum Ausführen von Befehlen in der cmd
import subprocess

# Um das Programm zu schließen, wenn die Konfigurations-Datei nicht gefunden werden konnte
import sys

# Zufällige Antworten
import random
# Um das Verzeichniss von diesem Skript herauszufinden
import pathlib


answerSuccessList = ['Ok, ich öffne nun', 'Ok, ich starte nun']
unableFindProgramAnswers = ['Sir, ich finde dieses Programm leider nicht.', 'Sir, ich kann dieses Programm leider nicht öffnen.']


def parseConfFile(textFile):
    pathDict = {}

    for line in textFile:
        
        parsedText = str(line).split(" & ")
        keyword = parsedText[0]
        path = parsedText[1]

        # Füge das neue Paar ins Dictionary ein, damit die dann abgefragt werden können
        pathDict[keyword] = path

    return pathDict


def open_program(program):
    # Alle buchstaben des programs, eingegeben vom User klein machen, um das Matching zu verbessern
    program = program.lower()

    # Öffne die Datei, die die Pfade anhand der Keywords enthält, Lesemodus
    try:
        # Die Datei befindet sich im gleichen Verzeichniss, also das Verzeichniss von diesem Skript (pathlib)
        textFile = open(str( pathlib.Path(__file__).parent.absolute() ) + r"\program_list.txt", "r")
    except:
        print("Ich finde die Konfigurations-Datei nicht!")
        sys.exit(0)

    # Get the pair keyword-program_path out of the conf_file (program_list.txt)
    pathDict = parseConfFile(textFile)


    try:
        # Bekomme den Pfad aus dem Dictionary anhand des Keywords vom Client
        path = pathDict[program]

        # Wichtig: Beim parsen wird bei allen (außer dem letzten Element, deswegen if not) noch eine neue Zeile hinzugefügt, diese wird hier gelöscht
        if not (program == list(pathDict)[-1]):
            path = path[:-1]

        subprocess.Popen(path)

        textFile.close()

        return random.choice(answerSuccessList) + " " + program

    # If the program isn't declared in the program_list.txt
    except KeyError:
        return random.choice(unableFindProgramAnswers)