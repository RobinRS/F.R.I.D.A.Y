from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from geopy.geocoders import Nominatim
import time
import os
import pathlib

time_sleep = 3

def getLocation():
    chrome_options = Options()
    chrome_options.add_argument("--use-fake-ui-for-media-stream")
    # Man soll den Browser nicht sehen, also; headless funktioniert nicht, da sonst gps nicht aktiviert wird!
    #chrome_options.add_argument("headless")  

    timeout = 20

    # Das Verzeichnis, in dem sich der Chrome-Driver (benötigt für Selenium) befindet: Ist das Script-Verzeichnis, also das selbe
    chrome_driver_path = str( str( pathlib.Path(__file__).parent.absolute() ) + r"\chromedriver.exe"   )
    print("Chrome-Driver Path:          ", chrome_driver_path)

    driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)
    driver.get("https://mycurrentlocation.net/")
    wait = WebDriverWait(driver, timeout)
    time.sleep(time_sleep)

    longitude = driver.find_elements_by_xpath('//*[@id="longitude"]')
    longitude = [x.text for x in longitude]
    longitude = str(longitude[0])
    latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')
    latitude = [x.text for x in latitude]
    latitude = str(latitude[0])
    driver.quit()

    coordinates = [latitude, longitude]
    return coordinates


def convert_to_location(coordinates):
    geolocator = Nominatim(user_agent="F.R.I.D.A.Y")
    location = geolocator.reverse(coordinates[0] + ',' + coordinates[1])

    print(location.raw)

    # Setze einen Antwort-Text aus der Addresse zusammen
    address = location.raw['address']

    # Unterscheide zwischen: männlich: weg,.. ; weblich: straße,..
    if("straße" in address['road']):
        result = "Laut GPS befinden sie sich gerade in der "+ address['road'] + ', ' + address['town'] + ', ' + address['state'] + ', ' + address['country'] + '.'

    elif("weg" in address['road']):
        result = "Laut GPS befinden sie sich gerade im "+ address['road'] + ', ' + address['town'] + ', ' + address['state'] + ', ' + address['country'] + '.'

    else:
        result = "Laut GPS befinden sie sich gerade in "+ address['road'] + ', ' + address['town'] + ', ' + address['state'] + ', ' + address['country'] + '.'
        
    return result

def cmd(entities):
    coordinates = getLocation()
    print(coordinates)
    return convert_to_location(coordinates)