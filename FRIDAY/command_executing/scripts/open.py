def url(urlEntitie):
    from . import open_website
    return open_website.open_website(urlEntitie)

def program(programEntitie):
    from . import open_program
    return open_program.open_program(programEntitie)

def cmd(entities):
    try:
        urlEntitie = entities['wit$url:url'][0]['body']
        return url(urlEntitie)
    except KeyError:
        try:
            programEntitie = entities['thing_to_open:thing_to_open'][0]['body']
            return program(programEntitie)
        except KeyError:
            return "I don't understand what i should open."
