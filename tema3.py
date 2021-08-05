import requests
from bs4 import BeautifulSoup as bs

URL = "https://www.allkeyshop.com/blog/buy-hollow-knight-cd-key-compare-prices/"
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"}


def check_webpage():
    page = requests.get(URL, headers=headers)
    soup = bs(page.content, 'html.parser')

    span_prices = soup.find_all('span')
    prices = []
    f = open("prices.txt", "a")
    for span in span_prices:
        if span.has_attr('class'):
            if "topclick-list-element-price" in span['class'][0]:
                price = span.text
                prices.append(price)
    for price in sorted(prices):
        print(price)
        f.write(price)

    f.close()


check_webpage()
