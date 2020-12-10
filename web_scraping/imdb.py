import requests
import bs4
url = "https://www.imdb.com/chart/top/"
page = requests.get(url)
soup = bs4.BeautifulSoup(page.text,'html.parser')
data = []
m_div = soup.find('div',{'class':'lister'})
tbody = m_div.find('tbody',{'class':'lister-list'})
trs = tbody.find_all('tr')
r = 0
for tr in trs:
   position = tr.find('td',{'class':'titleColumn'}).get_text().strip()
   r += 1
   name = tr.find('td',{'class':'titleColumn'}).a.text.strip()
   yr = tr.find('td',{'class':'titleColumn'}).span.text
   stars = tr.find('td',{'class':'ratingColumn imdbRating'}).strong.text
   link = tr.find('td',{'class':'titleColumn'}).a['href']
   m_link = "https://www.imdb.com" + link
   data.append({
       'rank':r,
       'title':name,
       'rel_year':yr,
       'rating':stars,
       'url':m_link
      })
         
#print(data)
import pandas as pd
df = pd.DataFrame(data)
print(df)
df.to_csv('imdb.csv',index = False)              

            