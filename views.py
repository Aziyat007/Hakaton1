import json
FILE_PATH = 'data.json'

def get_data():
    with open(FILE_PATH) as file:
        return json.load(file)

def retrieve_product():
    data = get_data()
    id = int(input('Enter id: '))
    product = (list(filter(lambda x: x['id'] == id, data)))
    if not product:
        return 'такого продукта нет'
    return product

def get_id():
    with open('id.txt', 'r') as file:
        id = int(file.read())
        id += 1
    with open('id.txt', 'w') as file:
        file.write(str(id))
    return id

def create_product():
    data = get_data()
    product = {
        'id': get_id(),
        'brand': input('Введите название бренда: '),
        'model': input('Введите модель ноутбука: '),
        'year of release': input('Введите год выпуска: '),
        'descrioption': input('Введите описание: '),
        'price' : round(float(input('Введите цену: ')), 2)
        }
    data.append(product)

    with open(FILE_PATH, 'w') as file:
        json.dump(data, file, indent=2)
        return 'CREATED'

def update_product():
    data = get_data()
    flag = False
    id = int(input('Enter product-id: '))
    product = list(filter(lambda x: x['id'] == id, data))
    if not product:
        return 'Такого продукта нет'
    index_ = data.index(product[0])
    choice_ = int(input('что вы хотите изменить? 1 - title, 2 - price: '))
    if choice_ == 1:
        data[index_]['title'] = input('Введите новое название продукта: ')
        flag = True
    elif choice_ == 2:
        data[index_]['price'] = input('Введите новый прайс: ')
        flag = True
    else:
        print('Такого поля нет')

    if flag:
        return 'UPDATED'
    else:
        return 'NOT UPDATED'

    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)

def delete_product():
    data = get_data()
    id = int(input('Введите id продукта: '))
    product = list(filter(lambda x: x[id] == id, data))
    if not product:
        return 'Такого продукта нет'
    index_ = data.index(product[0])
    data.pop(index_)

    json.dump(data, open(FILE_PATH, 'w'))

    return 'DELETED'