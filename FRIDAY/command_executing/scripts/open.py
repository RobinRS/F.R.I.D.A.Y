from .Function_Module import Function_Module

class open(Function_Module):
    name = "open"
    help_description = "Opens a website, or a program defined in program_list.txt."

    def url(self, urlEntitie):
        from . import open_website
        return open_website.open_website(urlEntitie)

    def program(self, programEntitie):
        from . import open_program
        return open_program.open_program(programEntitie)

    def respond(self, entities):
        try:
            urlEntitie = entities['wit$url:url'][0]['body']
            return self.url(self, urlEntitie)
        except KeyError:
            try:
                programEntitie = entities['thing_to_open:thing_to_open'][0]['body']
                return self.program(self, programEntitie)
            except KeyError:
                return "Sorry Sir, I don't understand what I have to open."