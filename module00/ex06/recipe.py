cookbook = {
    "sandwich" : {"ingredients" : ["ham", "bread", "cheese", "tomatoes"],
                  "meal" : "lunch",
                  "prep_time" : 10},
    "cake" : {"ingredients" : ["flour", "sugar", "eggs"],
                  "meal" : "dessert",
                  "prep_time" : 60},
    "salad" : {"ingredients" : ["avocado", "arugula", "tomatoes", "spinach"],
                  "meal" : "lunch",
                  "prep_time" : 15}
}

def print_recipe(cookbook):
    """boucle sur les clés de book"""
    for name in cookbook:
        print(name)

def print_complet_recipe(cookbook, name):
    """prends une recette et imprime les details"""
    if name not in cookbook:
        print("Recipe not found!")
        return()
    recipe = cookbook[name]
    print(f"Recipe for {name}:")
    print(f"Ingredients list: {recipe['ingredients']}.")
    print(f"To be eaten for lunch {recipe['meal']}.")
    print(f"Takes {recipe['prep_time']} minutes of cooking.")

def delete_recipe(cookbook, name):
    """prend un nom de recette, vérifie si elle existe et la supprime"""
    if name not in cookbook:
        print("Recipe not found!")
        return()
    else:
        del(cookbook[name])
        print("Recipe deleted!")

def add_recipe(cookbook):
    """Demander à l’utilisateur : un nom de recette, une liste d’ingrédients (saisie ligne par ligne), un type de repas, un temps de préparation"""
    name = input("Enter a name:\n")
    ingredients = []
    print("Enter ingredients:")
    while True :
        ing = input()
        if ing == "":
            break
        ingredients.append(ing)
    meal = input("Enter a meal type:\n")
    time_str = input("Enter a preparation time:\n")
    try:
        prept = int(time_str)
    except ValueError:
        print("AssertionError: argument is not an integer")
        return()
    cookbook[name] = {"ingredients":ingredients, "meal": meal, "prep_time":prept}


if __name__=="__main__":
    while(1):
        print("Welcome to the Python Cookbook!")
        print("List of available options:")
        print("    1: Add a recipe")
        print("    2: Delete a recipe")
        print("    3: Print a recipe")
        print("    4: Print the cookbook")
        print("    5: Quit\n\n")
        print("Please select an option:")

