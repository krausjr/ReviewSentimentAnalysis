# ReviewSentimentAnalysis

This application scrapes customer reviews for James Kraus while employed at Scheller's Fitness and Cycling from listen360, performs sentiment analysis on the reviews, and saves the reviews and analysis to an xlsx file. This application runs entirely from the command prompt/terminal.

__Required installations are as follows:__

Install boto3 for sentiment analysis.

```pip install boto3```

Install selenium for webscraping.

```pip install selenium```

Install pandas for storing information in data frames

```pip install pandas```

Install openpyxl to write dataframe to xlsx file

```pip install openpyxl```

Make sure you have Google Chrome Web Browser installed. Navigate to the URL and follow the instructions to download Chrome 

<link>https://www.google.com/chrome/<link>

The webpage containing the customer reviews is an infinite feed. Selenium and chromedriver make it possible to load more reviews in the feed by piloting a browser and sending commands to page down. For this to be possible, Chromedriver *must* be installed at a system rooted path.

Install chromedriver for automated browser control:

<link>https://chromedriver.chromium.org/downloads<link>

On *macOS devices*
1. download chromedriver from the URL above
2. unzip chromedriver and install it
3. open terminal and enter "sudo nano /etc/paths"
4. enter your password
5. enter the path of the chromedriver
6. press "CNTRL-x" to quit and "y" to save and enter to confirm

On *Windows devices*
1. download the chromedriver from the URL above
2. unzip chromedriver and install it
3. drag/drop the chromedriver file into your "C:\Windows" folder

Once all installations are complete, open a terminal window, cd the ReviewSentimentAnalysis directory, and run:

```python reviews.py```

AWS access keys can be provided upon request. Input AWS access keys when prompted.

The final data file will save as "reviews.xslx" into the ReviewSentimentAnalysis folder.

__Code Louisville project requirements met:__

- [x] Implement a “scraper” that can be fed a type of file or URL and pull information off of it.
- [x] Connect to an external/3rd party API and read data into your app.
- [x] Analyze text and display information about it.
- [x] Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program.
- [x] Use pandas, matplotlib, and/or numpy to perform a data analysis project. Ingest 2 or more pieces of data, analyze that data in some manner, and display a new result to a graph, chart, or other display.
