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


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_recipes()

    shop_list = {}

    for dish in dishes:
        if dish not in cook_book:
            continue
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name'],
            measure = ingredient['measure'],
            quantity = ingredient['quantity'] * person_count

            if ingredient_name in shop_list:
                shop_list[ingredient_name]['quantity'] += quantity
            else:
                shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
    return  shop_list


cook_book = read_recipes()
shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 6)

pprint(shop_list, width=120, indent=4, depth=3, sort_dicts=False)