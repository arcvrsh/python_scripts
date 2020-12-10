import requests
import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm


def get_page_soup(url):
    try:
        page = requests.get(url)
        if page.status_code == 200:
            return BeautifulSoup(page.text, 'lxml')
        else:
            print('\n error',page.status_code)
            return None
    except AssertionError as error:
        print(f"internet/domain error {error}")
        return None


def extract_products(soup):
    cards = soup.find_all('div',{'class':'_1UoZlX'})
    if len(cards) > 0:
        print("\n",len(cards),"products found")
        return cards
    else:
        print("products not found")
        return None


def parse_product(product):
    title = product.find('div',{'class':'_3wU53n'}).text.strip()
    try:
        price = product.find('div',{'class':'_1vC4OE _2rQ-NK'}).text
    except:
        price = None
    try:
        stars = product.find('div',{'class':'hGSR34'}).text
    except:
        stars = None

    try:
        reviews = product.find('span',{'class':'_38sUEc'}).text
    except:
        reviews = None
    return {'title':title,
            'price':price, 
            'stars':stars,
            'reviews':reviews
            }


if __name__ == "__main__":
    dataset = []
    for num in tqdm(range(1,100)):
        url = f'https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_6_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_6_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobiles&requestId=8454ff7d-4c8b-4443-87d2-afc43808ead4&as-backfill=on&page={num}'
        soup = get_page_soup(url)    
        if soup:
            product_list = extract_products(soup)
            if product_list:
                for product in tqdm(product_list):
                    data = parse_product(product)
                    dataset.append(data)
            else:
                print("no products | closing scraper")
                continue
        else:
            print("no page data | closing scraper")
            continue
    else:
        print("scraper closed")
    df = pd.DataFrame(dataset)
    print(df)
    df.to_csv('flipcart_mobiles.csv')
    print("saved successfully")