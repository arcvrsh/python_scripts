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
    except:
        print("internet/domain error")
        return None


def extract_products(soup):
    cards = soup.find_all('div',{'class':'_3liAhj'})
    if len(cards) > 0:
        print("\n",len(cards),"products found")
        return cards
    else:
        print("products not found")
        return None


def parse_product(product):
    title = product.find('a', {'class':'_2cLu-l'}).text.strip().replace(",",'')
    try:
        price = product.find('div',{'class':'_1vC4OE'}).text
    except:
        price=None
    try:
        stars = product.find('div',{'class':'hGSR34'}).text
    except:
        stars = None

    try:
        reviews = product.find("span",{'class':'_38sUEc'}).text[1:-1]
    except:
        reviews = None

    try:
        imglink = product.find('img',{'class':'_1Nyybr'}).attrs.get('src')
    except:
        imglink = None

    return {'title':title,
            'price':price, 
            'stars':stars,
            'reviews':reviews,
            'imglink':imglink}


if __name__ == "__main__":
    dataset = []
    for num in tqdm(range(1,100)):
        url = f'https://www.flipkart.com/search?q=mask&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={num}'
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
    df.to_csv('flipkart_face_masks.csv')
    print("saved successfully")