from collections import namedtuple


class Receipt:
    def total_price(self):
        ...


class Drink(Receipt):
    def __init__(self, *args):
        print(args)
        self.price = args[0]
        self.original_size = args[1]
        self.taken_size = args[2]
        self.count = self.convert_size_to_count()

    def convert_size_to_count(self):
        count = self.original_size // self.taken_size
        return count

    def total_price(self):
        self.count = self.convert_size_to_count()
        return self.count * self.price


class Meal(Receipt):
    def __init__(self, *args):
        super().__init__()
        self.price = args[0]
        self.count = args[3]

    def total_price(self):
        return self.count * self.price


def start(product):
    item = product.type(product.price, product.original_size, product.taken_size, product.count)
    print(f'Цена {item.__class__.__name__}: {item.total_price()}')


if __name__ == '__main__':
    item = namedtuple('Product', ('type', 'price', 'original_size', 'taken_size', 'count'))

    tea = item(Drink, 150, 250, 100, 0)
    bread = item(Meal, 20, 0, 0, 10)

    items_tuple = (tea, bread)

    for i in items_tuple:
        start(i)
