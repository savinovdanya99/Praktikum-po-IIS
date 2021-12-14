from colored_text import ColoredText
from dataclasses import dataclass
from enum import Enum


@dataclass()
class Item:
    name: str
    price: int
    remains: int = 100


class Menu(Enum):
    tea = Item('tea', 60)
    soup = Item('soup', 150)
    egg = Item('egg', 75)
    coffee = Item('coffee', 100)


class TaxiAction:
    def call(self):
        return 'Calling a taxi'

    def status(self):
        ...


class CafeActions:
    def __init__(self):
        self.order = list()
        self.menu = Menu
        self.items = {'tea': Menu.tea, 'coffee': Menu.coffee, 'egg': Menu.egg, 'soup': Menu.soup}

    def add_item_to_order(self, item):
        self.order.append(self.items[item].value.name)

    def remove_item_from_order(self, item):
        self.order.pop(self.order.index(item))

    def get_order(self):
        return self.order

    def get_menu(self):
        menu = tuple(item.value.name for item in tuple(self.items.values()))
        return menu


class Fasade:
    def __init__(self):
        self.cafe_action = CafeActions()
        self.taxi_action = TaxiAction()

    def visit_caffee(self):
        print(self.taxi_action.call())
        print("Looking a coffee's menu")
        print(f"Caffe Menu: {', '.join(self.cafe_action.get_menu())}")
        self.cafe_action.add_item_to_order('tea')
        self.cafe_action.add_item_to_order('egg')
        self.cafe_action.add_item_to_order('coffee')

        self.cafe_action.remove_item_from_order('tea')
        print('Making order')
        print(f'Your order: {", ".join(self.cafe_action.get_order())}')


if __name__ == '__main__':
    Fasade().visit_caffee()
