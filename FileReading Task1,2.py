def cook_book_creating():
    import re
    cook_book={}
    ingr_dict= {}
    temp_list= []
    with open('recipes.txt', 'r', encoding="utf-8") as file:
        dish_list = []
        flag = True #Флаг указывает на новое блюдо в словаре cook_book
        id = 0 #id для обращения к конкретному блюду в списке блюд
        # создаем списки с блюдами и ингр.
        for line in file:
            if flag == True: #создаем список блюд
                r_line = re.sub('[\t\r\n|]', "", line)
                dish_list += [r_line]
                flag = False
                continue
            elif line == "\n": #формируем cook_book
                flag = True #указатель нового блюда в cook_book
                cook_book[dish_list[id]]= temp_list
                id += 1
                temp_list=[]
                continue
            elif len(line) < 3:
                pass
            elif flag == False: #создаем списки и словари ингр.
                r_line=re.sub('[\t\r\n]', "", line)
                ing_list = (r_line.split('|'))
                ingr_dict['ingredient_name'] = ing_list[0]
                ingr_dict['quantity'] = ing_list[1]
                ingr_dict['measure'] = ing_list[2]
                temp_list.append(ingr_dict.copy())
                continue
            cook_book[dish_list[id]] = temp_list
    return cook_book
# cook_book_creating()
def get_shop_list_by_dishes(dishes, person_count):
    shop_list= {}
    temp_dict = {}
    for dish in dishes:
        if dish in cook_book_creating().keys(): #проверяем наличие блюда в cook_book
            for ingr in cook_book_creating().get(dish): #Исключаем повторения ингредиентов в shop_list
                if ingr.get('ingredient_name') not in shop_list.keys(): #заполняем shop_list
                    temp_dict['measure'] = ingr.get('measure')
                    temp_dict['quantity'] = int(ingr.get('quantity')) * person_count
                    shop_list[ingr.get('ingredient_name')]=temp_dict.copy()
                else:
                    # Обновляем значение quantity по повторяющемуся ингредиенту
                    for repetitive_ingr in shop_list.get(ingr.get('ingredient_name')):
                        shop_list.get(ingr.get('ingredient_name'))['quantity'] = shop_list.get(ingr.get('ingredient_name'))['quantity'] + (int(ingr.get('quantity')) * person_count)
        else:
            return "Такого блюда нет в кулинарной книге!"
    print(shop_list)
get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
