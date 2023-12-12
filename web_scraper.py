import requests
from bs4 import BeautifulSoup

def get_bbc_news_headlines():
    # URL of the BBC News website
    url = "https://www.bbc.com/news"

    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the HTML elements containing the news headlines
        headline_elements = soup.find_all('h3', class_='gs-c-promo-heading__title')

        # Extract and print the headlines
        headlines = [headline.text.strip() for headline in headline_elements]
        return headlines
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

# Get and print the BBC News headlines
headlines = get_bbc_news_headlines()

if headlines:
    print("BBC News Headlines:")
    for index, headline in enumerate(headlines, start=1):
        print(f"{index}. {headline}")

