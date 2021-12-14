import abc
from random import choice
from colored_text import ColoredText


class Cafe(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_total_price(self):
        ...

    @abc.abstractmethod
    def get_total_weights(self):
        ...


class Menu(Cafe):
    def __init__(self, price, count, weight):
        super().__init__()
        self._price = price
        self._count = count
        self._weight = weight

    def get_total_price(self):
        return self._price * self._count

    def get_total_weights(self):
        return self._count * self._weight


def make_order(order):
    for product in order.items():
        count = [1, 2, 3, 4]
        product_name = product[0]
        price = product[1][0]
        weight = product[1][1]
        count = choice(count)

        order = Menu(price=price, count=count, weight=weight)

        print(f'Продукт {product_name}: сумма заказа {ColoredText(order.get_total_price(), color_name="yellow")} = количество продуктов {count} * цену {price},  \n'
              f'Общий вес заказа {ColoredText(order.get_total_weights(), color_name="cyan")} = количество продуктов {count} * {weight}')


if __name__ == '__main__':
    order_1 = {'Coffee': (60, 200), 'Water': (75, 400), 'Tea': (40, 200)}
    order_2 = {'Break': (100, 200), 'Soup': (75, 250), 'Tea': (40, 200)}

    for order in [order_1, order_2]:
        make_order(order)
