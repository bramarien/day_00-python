cookbook = {
            'sandwich': {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
                         'meal': 'lunch', 'prep_time': '10'},
            'cake': {'ingredients': ['flour', 'sugar', 'eggs'],
                     'meal': 'dessert', 'prep_time': '60'},
            'salad': {'ingredients': ['avocado', 'arugula', 'tomatoes',
                      'spinach'], 'meal': 'lunch', 'prep_time': '15'},
            }


def aff_key():
    for key in cookbook.keys():
        print(key)


def aff_value():
    for recipe in cookbook.values():
        for value in recipe.values():
            print(value)


def aff_all():
    for key, recipe in cookbook.items():
        print(key)
        for recipe_key, value in recipe.items():
            print(recipe_key)
            print(value)


def aff_recipe(name):
    print("\nRecipe for %s:" % name)
    print("Ingredients list: %s" % cookbook[name]['ingredients'])
    print("To be eaten for %s" % cookbook[name]['meal'])
    print("Takes %s minutes of cooking." % cookbook[name]['prep_time'])


def del_recipe(name):
    del cookbook[name]


def add_recipe(name, ingredients, meal, prep_time):
    cookbook[name] = {'ingredients': ingredients,
                      'meal': meal, 'prep_time': prep_time}


def aff_cookbook():
    for key in cookbook.keys():
        aff_recipe(key)
        print("------------------------\n")


def aff_lobby():
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")


def main():
    while(1):
        aff_lobby()
        digit = input("your choice: ")
        if digit == '1':
            ing = []
            name = input("Enter the Name: ")
            nbing = input("Enter the Number of ingredients: ")
            if nbing.isdigit() == 1:
                for i in range(int(nbing)):
                    ing.append(input("Enter the name of ingredients: "))
                meal = input("Meal to eat this recipe: ")
                prep_time = input("Time to make this recipe (in minutes): ")
                add_recipe(name, ing, meal, prep_time)
            else:
                print("ERROR: plz enter a valid number of ingredients")
        elif digit == '2':
            del_recipe(input("Name the recipe you want to be delete: "))
        elif digit == '3':
            aff_recipe(input("Name of the choosen recipen: "))
        elif digit == '4':
            aff_cookbook()
        elif digit == '5':
            print("Cookbook closed")
            return
        else:
            print("ERROR: please type the corresponding number.")
            print("To exit, enter 5.")


main()
