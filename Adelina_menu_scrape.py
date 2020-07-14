import sys
import bs4 as bs
import urllib.request
import pandas as pd

from web_page_loader import WebPage

# URL of the restaurnat menue
url = 'https://app.upserve.com/s/adelinas-brooklyn'
page_to_scrape = WebPage(url)

# Use BeautifulSoup to parse the HTML
soup = bs.BeautifulSoup(page_to_scrape.html, 'html.parser')

title = []
desc = []

# find all dish titles from menu items
menu_items = soup.findAll('div', class_='menu-item-title')
for item in menu_items:
    title.append(item.text)

# find all dish descriptions from menu items
menu_item_descriptions = soup.findAll('div', class_='menu-item-description')
for item in menu_item_descriptions:
    desc.append(item.text)

res_df = pd.DataFrame({'dish':title, 'description':desc})

# store the result into CSV files.
res_df.to_csv('result.csv')