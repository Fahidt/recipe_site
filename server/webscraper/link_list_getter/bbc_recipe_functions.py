import requests 
from bs4 import BeautifulSoup



# This scrapes all available recipe links and applies the bbc html to the front
def bbc_ingredient_list(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    ingredients = soup.find(class_="gel-layout gel-layout--equal promo-collection")
    recipe_list = []
    for link in ingredients.find_all('a'):
        link_to_be_added = 'https://www.bbc.co.uk'
        link_to_be_added = link_to_be_added + link.get('href')
        recipe_list.append(link_to_be_added)
    return recipe_list


