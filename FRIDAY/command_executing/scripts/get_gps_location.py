from .Function_Module import Function_Module
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import selenium
from geopy.geocoders import Nominatim
import time
import os
import pathlib

class get_gps_location(Function_Module):
    name = "get_gps_location"
    help_description = "Current location"

    time_sleep = 2
    error = "Sir, I'm sorry I can't get my location."
    chrome_not_found_error = "Sir, I can't find the Chrome binaries. Make sure that C:\Program Files(x86)\Google\Chrome\Application\chrome.exe is present!"

    def respond(self, entities):
        try:
            coordinates = self.getLocation(self)
            return self.convert_to_location(self, coordinates)
        except selenium.common.exceptions.WebDriverException:
            return self.chrome_not_found_error
        except:
            return self.error

    def getLocation(self):
        chrome_options = Options()
        chrome_options.add_argument("--use-fake-ui-for-media-stream")
        # You shouldn't see the browser, so; headless does not work, otherwise gps will not be activated!
        # chrome_options.add_argument ("headless")

        timeout = 20

        # The directory in which the Chrome driver (required for Selenium) is located: Is the script directory, i.e. the same
        chrome_driver_path = str( str( pathlib.Path(__file__).parent.absolute() ) + r"\chromedriver.exe"   )
        print("Chrome-Driver Path:          ", chrome_driver_path)

        driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)
        driver.get("https://mycurrentlocation.net/")
        wait = WebDriverWait(driver, timeout)
        time.sleep(self.time_sleep)

        longitude = driver.find_elements_by_xpath('//*[@id="longitude"]')
        longitude = [x.text for x in longitude]
        longitude = str(longitude[0])
        latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')
        latitude = [x.text for x in latitude]
        latitude = str(latitude[0])
        driver.quit()

        coordinates = [latitude, longitude]
        return coordinates

    def convert_to_location(self, coordinates):
        geolocator = Nominatim(user_agent="F.R.I.D.A.Y")
        location = geolocator.reverse(coordinates[0] + ',' + coordinates[1])

        print(location.raw)

        # Compose an answer text from the address
        address = location.raw['address']

        # Street with 'the'
        if("street" in address['road'] or "road" in address['road']):
            result = "According to GPS, you are currently in the "+ address['road'] + ', ' + address['town'] + ', ' + address['state'] + ', ' + address['country'] + '.'

        else:
            result = "According to GPS, you are currently in "+ address['road'] + ', ' + address['town'] + ', ' + address['state'] + ', ' + address['country'] + '.'
            
        return result