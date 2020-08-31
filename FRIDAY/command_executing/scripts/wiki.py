import wikipedia
from googletrans import Translator

sentences = 3

def cmd(entities):
    # Get the info to search in wikipedia, extracted as entity
    try:
        infoToSearch = entities['info:info'][0]['body']
    except:
        return "Nach wem wem wollen sie suchen, Sir?"
    
    # Erzähl mir etwas über dich ---> personality
    if (infoToSearch == "dich"):
        from . import personality
        return personality.cmd(None)
    
    translator = Translator()
    # Übersetze den deutschen Suchbegriff ins Englische und Suche im en-wikipedia. Übersetze den englischen Text wieder ins Deutsche
    wikipedia_search = translator.translate(infoToSearch, dest='en').text
    wikipedia_result = wikipedia_get(wikipedia_search, sentences)
    result = translator.translate(wikipedia_result, dest='de').text
    return result


def wikipedia_get(search, sentences):
    result = wikipedia.summary(search, sentences = sentences)
    return result