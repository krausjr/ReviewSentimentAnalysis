# This module displays customer reviews for James Kraus while employed at Scheller's Fitness and Cycling
# and performs sentiment analysis on the reviews.

# Install boto3 for sentiment analysis -- pip install boto3
# Install selenium for webscraping -- pip install selenium
# Install chromedriver in system PATH for automated browser control: https://chromedriver.chromium.org/downloads

# Import required packages
import time
import boto3
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Add options on chromedriver. These options allow selenium to do its work without opening the 
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
# Note: increase no_of_pagedowns to load more reviews

no_of_pagedowns = float(input("Input number between 1-100. Higher numbers load more reviews.\n"))

while no_of_pagedowns:
    element.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.05)
    no_of_pagedowns-=1

# Locate reviews that contain the name "James", save as string in json, 
# append json strings to list, print list of reviews.
reviews=[]
review_elements = browser.find_elements_by_xpath("//*[contains(text(), 'James')]")
for review in review_elements:
    json_string = json.dumps(review.text)
    reviews.append(json_string)
print(*reviews, sep='\n')

# Sentiment analysis of each review.
# Insert AWS API keys accordingly.

access_key = input("INPUT ACCESS KEY\n")
secret_access_key= input("INPUT SECRET ACCESS KEY\n")

comprehend = boto3.client(
    'comprehend', 'us-east-2',
    aws_access_key_id = access_key,
    aws_secret_access_key = secret_access_key
)

print('Calling DetectSentiment')
print(json.dumps(comprehend.batch_detect_sentiment(TextList=reviews, LanguageCode='en'), sort_keys=True, indent=4))
print('End of DetectSentiment\n')

browser.quit()