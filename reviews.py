# This module displays customer reviews for James Kraus while employed at Scheller's Fitness and Cycling.

# pip install selenium
# brew install chromedriver

# Import required packages
import time
import boto3
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Add options on chrome. These options allow selenium to do its work without opening the 
# browser window, thus speeding up the module.
chromeOptions = Options()
chromeOptions.add_argument("--headless")
chromeOptions.add_argument("--disable-gpu")


# Open chrome browser, navigate to listen360 URL, and locate the HTML body element.
browser = webdriver.Chrome(options=chromeOptions)
browser.get("https://reviews.listen360.com/scheller-s-fitness-cycling-middletown-louisville")
time.sleep(1)

element = browser.find_element_by_tag_name("body")

# Scroll down on page to load older reviews on the infinite feed.
no_of_pagedowns = 1

while no_of_pagedowns:
    element.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.05)
    no_of_pagedowns-=1

# Find and print only the reviews that contain the name "James"
# reviews = []
review_elements = browser.find_elements_by_xpath("//*[contains(text(), 'James')]")
for review in review_elements:
    json_string = json.dumps(review.text)
    print(json_string)

# for review in review_text:
#     reviews.append(review.text)

# test_reivew = reviews[0]
# print(type(test_reivew))

comprehend = boto3.client(service_name='comprehend', region_name='region')

print('Calling DetectSentiment')
print(json.dumps(comprehend.detect_sentiment(Text=json_string, LanguageCode='en'), sort_keys=True, indent=4))
print('End of DetectSentiment\n')

browser.quit()