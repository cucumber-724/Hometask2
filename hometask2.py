from pprint import pprint


def read_recipes():
    cook_book = {}
    with open('recipes.txt', 'r', encoding='utf-8') as f:
        while True:
            dish_name = f.readline().strip()
            if not dish_name:
                break
            ingredient_count = int(f.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_info = f.readline().strip().split(' | ')
                ingredient = {
                    'ingredient_name': ingredient_info[0],
                    'quantity': int(ingredient_info[1]),
                    'measure': ingredient_info[2]
                }
                ingredients.append(ingredient)
            cook_book[dish_name] = ingredients
            f.readline()
        return cook_book


cook_book = read_recipes()
pprint(cook_book, width=120, indent=4, depth=3, sort_dicts=False)
