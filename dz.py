
with open('recipes.txt', encoding='utf-8') as f:
    cook_book = {}
    recipes_lines = f.read().strip().split("\n")
    i = 0
    while i < len(recipes_lines):
        if recipes_lines[i] == '':
            i += 1
        dish_name = recipes_lines[i]
        i += 1
        amount_ingredients = int(recipes_lines[i])
        i += 1
        ingredients = []
        for _ in range(amount_ingredients):
           ingredients_line = recipes_lines[i]
           i += 1
           ingredient_name, quantity, measure = ingredients_line.strip().split('|')
           ingredients.append({'ingredient_name': ingredient_name,'quantity': int(quantity),'measure': measure})
        cook_book[dish_name] = ingredients
      
def get_shop_list_dy_dishes(dishes, person_count):
    shop_dist = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for name in cook_book[dish]:
                ing_name = name['ingredient_name']
                quantity_person = name['quantity'] * person_count
                count_ing = {'measure': name['measure'], 'quantity': quantity_person}
                shop_dist[ing_name] = count_ing
        else:
            return print(f'Данного блюда - {dish}, нет в меню')
    return print(shop_dist)


