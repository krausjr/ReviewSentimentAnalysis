#this project displays five star google reviews for James Kraus while employed at Scheller's Fitness and Cycling.

# Import required packages
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Add options on chrome
chromeOptions = Options()
chromeOptions.add_argument("--headless")
chromeOptions.add_argument("--disable-gpu")


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

review_elements = browser.find_elements_by_xpath("//*[contains(text(), 'James')]")

# review_elements = browser.find_elements_by_class_name("listen360-feedback-summary-span")

for review in review_elements:
    print(review.text)

# page_source_overview = browser.page_source

# from bs4 import BeautifulSoup

# # Load in page source info
# soup = BeautifulSoup(page_source_overview, 'lxml')

# # text_to_search = soup.find_all('span', class_='listen360-feedback-summary-span')

# reviews = soup.find_all("span", string="James")

# print(len(reviews))

# for review in reviews:
#     print(reviews)

# browser.quit()