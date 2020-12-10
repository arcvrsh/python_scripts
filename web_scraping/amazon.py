import requests
import pandas as pd
from bs4 import BeautifulSoup
import tqdm

def get_page_soup(url):
    try:
        page = requests.get(url)
        if page.status_code == 200:
            return BeautifulSoup(page.text,'lxml')
        else:
            print('\n error',page.status_code)
            return None
    except:
        print("internet/domain error")
        return None

def extract_products(soup):
    