#this project displays five star google reviews for James Kraus while employed at Scheller's Fitness and Cycling.

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://reviews.listen360.com/scheller-s-fitness-cycling-middletown-louisville")
time.sleep(1)

elem = browser.find_element_by_tag_name("body")

no_of_pagedowns = 20

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1

post_elems = browser.find_elements_by_class_name("listen360-feedback-summary-span")

for post in post_elems:
    print(post.text)