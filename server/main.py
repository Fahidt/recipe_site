from webscraper.webscrapers.bbc_ingredient_scraper import ingredient_scraper
from webscraper.recipe_details.bbc_recipe_dict import bbc_recipe_dict
from pprint import pprint



indian_links = bbc_ingredient_list('https://www.bbc.co.uk/food/search?q=indian')
indian_list = []
failed_links = []

for i in indian_links:
    try:
        indian_list.append(ingredient_scraper(i))
    except:
        failed_links.append(i)

pprint(indian_list)
print(failed_links)


