from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from textblob import TextBlob
import time

def get_financial_news(query="Tesla", max_pages=3):
    # Set up Selenium with headless Chrome
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")

    # Initialize the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    news = []

    for page in range(max_pages):
        # Update the URL with the `start` parameter for pagination
        start = page * 10
        url = f"https://www.google.com/search?q={query}+news&tbm=nws&start={start}"
        driver.get(url)

        # Wait for the page to load
        time.sleep(2)

        # Extract news articles
        articles = driver.find_elements(By.CLASS_NAME, "SoaBEf")
        for article in articles:
            try:
                # Extract the title
                title_element = article.find_element(By.CLASS_NAME, "n0jPhd.ynAwRc.MBeuO.nDgy9d")
                title = title_element.text

                # Extract the snippet
                snippet_element = article.find_element(By.CLASS_NAME, "GI74Re.nDgy9d")
                snippet = snippet_element.text

                # Append the data to the news list
                news.append({"title": title, "snippet": snippet})
            except Exception as e:
                print(f"Error extracting article: {e}")

    driver.quit()
    return news

def analyze_sentiments(news):
    for article in news:
        analysis = TextBlob(article['snippet'])
        polarity = analysis.sentiment.polarity
        if polarity > 0:
            sentiment = "Positif"
        elif polarity < 0:
            sentiment = "Négatif"
        else:
            sentiment = "Neutre"
        article['sentiment'] = sentiment
    return news

# Main execution
news = get_financial_news(max_pages=4)  # Scrape 3 pages of news
news_with_sentiments = analyze_sentiments(news)

# Print the results
for article in news_with_sentiments:
    print(f"Title: {article['title']}")
    print(f"Snippet: {article['snippet']}")
    print(f"Sentiment: {article['sentiment']}")
    print("-" * 50)

print(f"Total articles scraped: {len(news_with_sentiments)}")