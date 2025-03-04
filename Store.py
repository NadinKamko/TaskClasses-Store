# Ты разрабатываешь программное обеспечение для сети магазинов.
# Каждый магазин в этой сети имеет свои особенности,
# но также существуют общие характеристики, такие как адрес, название и ассортимент товаров.
# Ваша задача — создать класс Store, который можно будет использовать для создания различных магазинов

class Store():
    def __init__(self, name, address):
        self.name = name
        self.assress = address
        self.items = {}

    # метод добавления товара в ассортимент
    def add_item(self, item_name, price):
        self.items[item_name] = price

    # удаление товара из списка
    def remove_item(self, item_name):
        self.items.pop(item_name, None)

    # получение цены товара по его названию
    def get_price(self, item_name):
        return self.items.get(item_name)

    # обновление цены товара
    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

# создание объектов (магазинов) класса Store
store1 = Store('Магнит', 'ул. Петушкова 7')
store1.add_item('яблоки', 75.0)
store1.add_item('бананы', 80.0)

store2 = Store('Пятерочка', 'ул. Пушкина 5')
store2.add_item('хлеб', 40.0)
store2.add_item('молоко', 60.0)

store3 = Store('Азбука вкуса', 'ул. Павлова 13')
store3.add_item('колбаса', 200.0)
store3.add_item('сыр', 180.0)

# тестирование метода на примере 2
print('Тестирование методов для магазина: ', store2.name)
print('Изначальный ассортимент: ', store2.items)

# добавление товара
store2.add_item('печенье', 50.0)
print('\nПосле добавления печенья: ', store2.items)
# обновление цены
store2.update_price('хлеб', 42.0)
print('\nЦена хлеба после обновления: ', store2.get_price('хлеб'))
# удаление товара
store2.remove_item('молоко')
print('\nПосле удаления молока: ', store2.items)