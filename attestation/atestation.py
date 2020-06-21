"""Task for attestation 'hqcnqvnx'."""
import itertools
from typing import Any


class OutOfResourceError(Exception):
    """Create Exception Class."""

    def __init__(self: Any, message: str) -> None:
        super().__init__(message)


class CoffeMaschin:
    """Crete new class for making coffe."""

    def __init__(self: Any, dictionary: list) -> None:
        self.dictionary = dictionary
        self.total_quantity=[]


    def calculate(self: Any):
        """Calculate ingridients."""
        for item in self.dictionary:
            for key in item:
                if item.get(key) == "кофе":
                    if int(item.get('количество'))>int(item.get('порция')):
                        coffe_dict={item.get(key):item.get('ресурс')}
                        self.total_quantity.append(coffe_dict)
                    else:
                        raise OutOfResourceError("not enought coffe")
                elif item.get(key) == "вода" and key=='тип':
                    if int(item.get('количество')) > int(item.get('порция')):
                        water_dict = {item.get(key): item.get('ресурс')}
                        self.total_quantity.append(water_dict)
                    else:
                        raise OutOfResourceError("not enought coffe")
                elif item.get(key) == "молоко" and key=='тип':
                    if int(item.get('количество')) > int(item.get('порция')):
                        milk_dict = {item.get(key): item.get('ресурс')}
                        self.total_quantity.append(milk_dict)

                elif item.get(key) == "сироп":
                    if int(item.get('количество')) > int(item.get('порция')):
                        sirop_dict={item.get(key): item.get('ресурс')}
                        self.total_quantity.append(sirop_dict)
        print(self.total_quantity)

    def menu(self):
        coffe = []
        sirop = []
        milk = []
        water = []
        for item in self.total_quantity:
            for key in item:
                if key == 'кофе':
                    coffe.append(item)
                elif key == 'сироп':
                    sirop.append(item)
                elif key == 'вода':
                    water.append(item)
                elif key == 'молоко':
                    milk.append(item)

        result = list(itertools.product(coffe, water))+list(itertools.product(coffe, water,milk))\
                 +list(itertools.product(coffe, water,sirop))+list(itertools.product(coffe, water, sirop, milk))

        return result


if __name__ == '__main__':
    a=CoffeMaschin([
    {
        "ресурс" : "арабика",
        "тип" : "кофе",
        "количество" : 1000,
        "порция" : 10
    },
    {
        "ресурс": "робуста",
        "тип": "кофе",
        "количество": 1000,
        "порция": 10
    },

    {
        "ресурс" : "вода",
        "тип" : "вода",
        "количество" : 1000,
        "порция" : 60
    },
    {
        "ресурс" : "карамель",
        "тип" : "сироп",
        "количество" : 200,
        "порция" : 80
    },
    {
        "ресурс" : "шоколад",
        "тип" : "сироп",
        "количество" : 200,
        "порция" : 80
    }
])
    a.calculate()
    print(a.menu())