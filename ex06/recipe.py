#!/goinfre/archid-/miniconda3/bin/python3.10
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: 0x0584 <archid-@1337.student.ma>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/02/18 21:21:35 by 0x0584            #+#    #+#              #
#    Updated: 2023/02/20 20:04:38 by archid           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
from sys import argv

cookbook_info = ['ingredients', 'meal', 'prep_time']
# Cookbook singleton
cookbook = dict(
    Sandwich=dict(
        ingredients=['ham', 'bread', 'cheese', 'tomatoes'],
        meal='lunch', prep_time=10),
    Cake=dict(
        ingredients=['flour', 'sugar', 'eggs'],
        meal='dessert', prep_time=60),
    Salad=dict(
        ingredients=['avocado', 'arugula', 'tomatoes', 'spinach'],
        meal='dessert', prep_time=60),
)

def print_recipes():
    """
    Prints the names of the recipes
    """
    global cookbook
    for recipe in cookbook.keys():
        print(recipe)

def print_recipe(recipe: str):
    """
    Prints the ingrediants of a recipe that is identified by
    the key `recipe' in the Cookbook
    """
    global cookbook
    assert recipe in cookbook.keys(), "recipe not in cookbook"
    for recipe_info in cookbook[recipe]:
        for info in cookbook_info:
            print("{}: {}".format(info, recipe[info]))

def erase_recipe(recipe: str):
    """
    Erases a recipe from the Cookbook
    """
    global cookbook
    assert recipe in cookbook.keys(), "recipe not in cookbook"
    cookbook.pop(recipe)

def add_recipe(recipe=None, ingredients=None, meal_type=None, prep_time=None):
    """
    Adds a recipe to the Cookbook, or may ask for input in case any information was omitted
    """
    if recipe is None:
        recipe = input(">>> Enter a recipe:")
    else:
        assert type(recipe) == str, "recipe should be string"

    if ingredients is None:
        print(">> Enter ingredients:", end='')
        ingredients = list()
        while True:
            e = input("")
            if len(e) == 0:
                break;
            ingredients += e
    else:
        for i in ingredients:
            assert type(i) == str, "ingredient should be a string"

    if meal_type is None:
        meal_type = input(">>> Enter a meal type:")
    else:
        assert type(meal_type) == str

    if prep_time is None:
        try:
            prep_time = int(input(">>> Enter a preparation time:"))
        except ValueError:
            assert false, "preparation time should be a numeric"
    else:
        assert type(prep_time) == int

    global cookbook
    cookbook[recipe] = dict(
        ingredients=ingredients, meal_type=meal_type, prep_time=prep_time)

if __name == ' __main__':
    argc = len(argv)
    print("Welcome to the Python Cookbook !\n"
          "List of available options:\n"
          "\t1: Add a recipe\n"
          "\t2: Delete recipe\n"
          "\t3: Print a recipe\n"
          "\t4: Print the cookbook"
          "\t5: Quit\n")
    while True:
        try:
            option = int(input("Please select an option\n>> "))
            assert 5 >= option >= 1, "options are from 1-5"
        except ValueError:
            assert False, "you must select an option number"

        if option == 1:
            print("Please fill recipe information to add it:")
            add_recipe()
        elif option == 2:
            print("Please enter a recipe name to delete it:")
            erase_recipe(input(">> "))
        elif option == 3:
            print("Please enter a recipe name to get its details:")
            print_recipe(input(">> "))
        elif option == 4:
            print_recipes()
        elif option == 5:
            pass
