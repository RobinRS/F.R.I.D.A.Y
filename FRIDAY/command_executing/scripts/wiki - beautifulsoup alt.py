from bs4 import BeautifulSoup
import requests

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


    # Get the wikipedia-entry and parse the first block of text
    website = "https://de.wikipedia.org/wiki/" + str(infoToSearch)

    source = requests.get(website).text
    soup = BeautifulSoup(source, 'lxml')

    for div in soup.find_all('div', class_ = "mw-parser-output"):
        summary = div.p.text
        print(summary)

    print()
    print()
    print()

    # Lösche alle Inhalte mit [eckigen Klammern], da diese unleserliche unnötige Informationen beinhalten (z.B. Lautschrift, Audio-Beispiel)
    """ c = '['
    # for c in summary:
    #     tmp1 = summary.split("[")[1]
    #     summary = summary.replace(tmp1, '')

    tmp1 = summary.split("[")[1]
    tmp2 = summary.replace(tmp1, '')
    tmp3 = tmp2.split(c)[2]
    tmp4 = tmp2.replace(tmp3 , '')
    tmp5 = tmp4.split(']')[1]
    print(tmp5) """

    return summary
