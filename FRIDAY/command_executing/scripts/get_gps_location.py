# Returns your location based on the website mycurrentlocation.net which uses gps
# Parses this website with selenium


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

    timeout = 20

    # The directory in which the Chrome driver (required for Selenium) is located: Is the script directory, i.e. the same
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

    # Put together an answer text from the address
    address = location.raw['address']

    result = "According to GPS, you are currently in "+ address['road'] + ', ' + address['town'] + ', ' + address['state'] + ', ' + address['country'] + '.'
        
    return result

def cmd(entities):
    coordinates = getLocation()
    print(coordinates)
    return convert_to_location(coordinates)
