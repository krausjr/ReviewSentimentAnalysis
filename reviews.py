#this project displays five star google reviews for James Kraus while employed at Scheller's Fitness and Cycling.

# Import required packages
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Add options on chrome
chromeOptions = Options()
# chromeOptions.add_argument("--headless")
# chromeOptions.add_argument("--disable-gpu")


# locate elements by name
browser = webdriver.Chrome(options=chromeOptions)
browser.get("https://reviews.listen360.com/scheller-s-fitness-cycling-middletown-louisville")
time.sleep(1)

element = browser.find_element_by_tag_name("body")

no_of_pagedowns = 10

while no_of_pagedowns:
    element.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1

# post_elements = browser.find_elements_by_class_name("listen360-feedback-summary-span")

# for post in post_elements:
#     print(post.text)

page_source_overview = browser.page_source