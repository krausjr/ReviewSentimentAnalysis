# ReviewSentimentAnalysis

This application displays customer reviews for James Kraus while employed at Scheller's Fitness and Cycling
and performs sentiment analysis on the reviews.

The required installs are as follows:
Install boto3 for sentiment analysis.

-- pip install boto3

Install selenium for webscraping.

-- pip install selenium

Install openpyxl to write dataframe to xlsx file

--pip install openpyxl


Install Google Chrome web browser.

The URL passed to selenium for web scraping is an infinite feed of customer reviews. Selenium and chromedriver load more reviews in the feed. Chromedriver must be installed at a system rooted path in order to pilot a chrome browser window. 
Install chromedriver for automated browser control:

https://chromedriver.chromium.org/downloads

On macOS devices this can be accomplished with the following steps:
1) download chromedriver from the URL above
2) unzip chromedriver and install it
3) open terminal and enter "sudo nano /etc/paths"
4) enter your password
5) enter the path of the chromedriver
6) press "CNTRL-x" to quit and "y" to save and enter to confirm

On Windows devices, simply download the chromedriver, unzip the download, and drag/drop the file into your Windows folder.

Code Louisville project requirements met:
1) Implement a “scraper” that can be fed a type of file or URL and pull information off of it. For example, a web scraper that lets you provide any website URL and it will find certain keywords on the page.
2) Analyze text and display information about it (ex: how many words in a paragraph).
3) Connect to an external/3rd party API and read data into your app.
4) Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program.
5) Use pandas, matplotlib, and/or numpy to perform a data analysis project. Ingest 2 or more pieces of data, analyze that data in some manner, and display a new result to a graph, chart, or other display.
6) Visualize data in a graph, chart, or other visual representation of data.
7) Create and call at least 3 functions or methods, at least one of which must return a value that is used somewhere else in your code.
