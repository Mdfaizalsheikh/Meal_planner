import random
import json


class Recipe:
    def __init__(self, name, ingredients, dietary_restrictions):
        self.name = name
        self.ingredients = ingredients
        self.dietary_restrictions = dietary_restrictions


def load_recipes(filename):
    try:
        with open(filename, 'r') as f:
            recipes = json.load(f)
            return [Recipe(**recipe) for recipe in recipes]
    except FileNotFoundError:
        return []

def save_recipes(recipes, filename):
    with open(filename, 'w') as f:
        json.dump([recipe.__dict__ for recipe in recipes], f)


def add_recipe():
    name = input("Enter the recipe name: ").strip()
    ingredients = input("Enter the ingredients (comma-separated): ").strip().split(',')
    dietary_restrictions = input("Enter dietary restrictions (comma-separated): ").strip().split(',')
    recipes.append(Recipe(name, ingredients, dietary_restrictions))
    save_recipes(recipes, filename)
    print("Recipe added successfully!")

def suggest_meals(dietary_restrictions):
    meal_plan = {}
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    filtered_recipes = [recipe for recipe in recipes if not any(restriction in recipe.dietary_restrictions for restriction in dietary_restrictions)]

    for day in days_of_week:
        meal_plan[day] = random.choice(filtered_recipes).name if filtered_recipes else "No suitable recipes found"
    return meal_plan

def display_meal_plan(meal_plan):
    print("\nMeal Plan for the Week:")
    for day, meal in meal_plan.items():
        print(f"{day}: {meal}")


if __name__ == "__main__":
    filename = 'recipes.json'
    recipes = load_recipes(filename)

    while True:
        print("\nMeal Planner")
        print("1. Add a new recipe")
        print("2. Suggest meals for the week")
        print("3. Quit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_recipe()
        elif choice == '2':
            dietary_restrictions = input("Enter your dietary restrictions (comma-separated): ").strip().split(',')
            meal_plan = suggest_meals(dietary_restrictions)
            display_meal_plan(meal_plan)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
