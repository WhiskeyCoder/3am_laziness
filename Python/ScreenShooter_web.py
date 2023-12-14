from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re

options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
driver = webdriver.Chrome(chrome_options=options, service=Service(ChromeDriverManager().install()))

target = './websites.txt'
lineList = [line.rstrip('\n') for line in open(target, "r")]
for line in lineList:

    try:
        target = line
        driver.get("https://" + target)
        sleep(3)
        print("capturing " + line)
        fn = target.replace("/", "")
        fn = fn.replace(":", "")
        driver.get_screenshot_as_file("./shots/" + fn + ".png")
    except:
        print(line + " not scrapabale")
driver.quit()
