# number1
import json

files = 'Downloads/lab.json'
with open(files, 'r') as file:
    data = json.load(file)
products = data['products']

p_name = input('Введите название : ')
p_price = int(input('Введите цену : '))
p_available = True if input('Продукт доступен? (Да/Нет): ').lower() == 'да' else False
p_weight = int(input('Введите вес : '))

products.append({
    "name": p_name,
    "price": p_price,
    "available": p_available,
    "weight": p_weight
})

# обновление данных в файле
with open('Downloads/lab.json', 'w') as file:
    json.dump(data, file, indent=4)

for product in products:
    name = product['name']
    price = product['price']
    available = 'В наличии' if product['available'] else 'Нет в наличии!'
    weight = product['weight']

    print(f"Название: {name}")
    print(f"Цена: {price}")
    print(f"Вес: {weight}")
    print(f"{available}")
    print()

# number3
def new_f():
    ru_eng_dict = {}
    with open('Downloads/eng-ru.txt', 'r', encoding="utf-8") as file:
        chit = file.readlines()
        for line in chit:
            eng_words, ru_words = line.strip().split(' - ')
            list_ru = ru_words.split(', ')
            for ru_word in list_ru:
                if ru_words not in ru_eng_dict:
                    ru_eng_dict[ru_words] = [eng_words]
                else:
                    ru_eng_dict[ru_words].append(eng_words)
    with open('Downloads/ru-eng.txt', 'w', encoding="utf-8") as file:
        for ru_word in sorted(ru_eng_dict.keys()):
            eng_words_str = ', '.join(sorted(ru_eng_dict[ru_word]))
            file.write(f"{ru_word} - {eng_words_str}\n")

new_f()


