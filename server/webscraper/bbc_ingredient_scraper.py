import requests 
from bs4 import BeautifulSoup


def ingredient_scraper(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(class_='recipe-ingredients__list')
    listed_items = results.find_all('li')
    ingredient_list = []
    for li in listed_items:
        ingredient_list.append(li.text)
    
    return ingredient_list
