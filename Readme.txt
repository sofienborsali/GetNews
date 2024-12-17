Project Title
Google News Scraper with Sentiment Analysis and Stock Data Fetcher

Description
This project is a Python-based web scraper that extracts financial news articles from Google News and performs sentiment analysis on the snippets using the TextBlob library. Additionally, it includes functionality to fetch historical stock data from Yahoo Finance. The project uses Selenium for web scraping and BeautifulSoup for parsing HTML.

Features
Scrapes financial news articles from Google News for a given query.
Analyzes the sentiment of each news snippet (Positive, Negative, or Neutral).
Fetches historical stock data (date, open price, and close price) for a given stock symbol from Yahoo Finance.
Supports pagination to scrape multiple pages of Google News results.

How to Use
1. Clone the Repository
git clone https://github.com/sofienborsali/GetNews.git
cd your-repository-name
2. Install Required Libraries
Make sure you have Python installed. Then, install the required libraries using pip:

pip install selenium webdriver-manager textblob beautifulsoup4 requests

3. Run the Script
Run the script to scrape financial news, analyze sentiments, and fetch stock data:
python your_script_name.py

4. Output
The script will print the financial news articles with their sentiment analysis.
It will also print the historical stock data for the specified stock symbol.
Required Libraries
The following Python libraries are required:

Selenium: For web scraping dynamic content.
pip install selenium
Webdriver Manager: To manage the Chrome WebDriver.
pip install webdriver-manager
TextBlob: For sentiment analysis.
pip install textblob
BeautifulSoup: For parsing HTML content.
pip install beautifulsoup4
Requests: For making HTTP requests.
pip install requests
