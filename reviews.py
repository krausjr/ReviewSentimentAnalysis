# This module displays customer reviews for James Kraus while employed at Scheller's Fitness and Cycling
# and performs sentiment analysis on the reviews.

# Import required packages
import time
import boto3
import json
import pandas as pd
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
def load_reviews():
    no_of_pagedowns = float(input("Type an integer between 1-200. Higher numbers load more reviews.\n")) 

    while no_of_pagedowns:
        element.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
        no_of_pagedowns-=1

# Locate reviews that contain the name "James", save as string in json, 
# append json strings to list, and create review dataframe.
def find_reviews():
    review_elements = browser.find_elements_by_xpath("//*[contains(text(), 'James')]")
    for review in review_elements:
        json_string = json.dumps(review.text)
        reviews_df.loc[len(reviews_df.index)] = [json_string]
        reviews.append(json_string)

reviews=[]
reviews_df= pd.DataFrame(columns=['review_text'])

# Sentiment analysis of each review. Merge dataframes for review text and sentiment analysis.
def detect_sentiment():
    access_key = input("INPUT ACCESS KEY\n")
    secret_access_key= input("INPUT SECRET ACCESS KEY\n")

    comprehend = boto3.client(
        'comprehend', 'us-east-2',
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_access_key) 

    sentiment_json = comprehend.batch_detect_sentiment(TextList=reviews, LanguageCode='en')

    json.dumps(sentiment_json)
    df1=pd.json_normalize(sentiment_json, record_path=['ResultList'])

    frames = [df1, reviews_df]
    final_df = pd.concat(frames, axis=1)
    
    pd.DataFrame.to_excel(final_df, excel_writer='reviews.xlsx')

def main():
    load_reviews()
    find_reviews()
    detect_sentiment()

main()

browser.quit()