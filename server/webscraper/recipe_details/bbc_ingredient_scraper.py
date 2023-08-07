import requests 
from bs4 import BeautifulSoup

# get name 
def bbc_recipe_dict(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    recipe_name = soup.find(class_="gel-trafalgar content-title__text").text
    recipe_name = {"Preparation time":"",
                   "Cooking time":"",
                   "Serves":"", 
                   "Description":"",
                   "Ingredients":[],
                   "Method":[]
                }
    
    # Information on Preparation time
    prep_time = soup.find(class_="recipe-metadata__prep-time").text
    recipe_name["Preparation time"] = prep_time

    # Cooking time
    cook_time = soup.find(class_="recipe-metadata__cook-time").text
    recipe_name["Cooking time"] = cook_time

    # Serves
    serve = soup.find(class_="recipe-metadata__serving").text
    recipe_name["Serves"] = serve

    # Recipe brief description
    recipe_desc = soup.find(class_="recipe-description__text").text.replace('\r\n','')
    recipe_name["Description"] = recipe_desc

    # ingredients 
    recipe = soup.find(class_='gel-layout recipe-ingredient-list')
    listed_ingredients = recipe.find_all('li')
    ingredient_list = []
    for ingredient in listed_ingredients:
        recipe_name["Ingredients"].append(ingredient.text)
    
    # method of cooking 
    method = soup.find(class_='recipe-method__list')
    listed_steps = method.find_all('li')
    steps = []
    for steps in listed_steps:
        recipe_name["Method"].append(steps.text)
    
    return recipe_name


# Create a dictionary for the the data to be stored, for testing only. 
recipe_complete_details = {}

poop = bbc_recipe_dict('https://www.bbc.co.uk/food/recipes/vegan_mac_and_cheese_32466')
print(poop)

