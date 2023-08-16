class Flower:
    def __init__(self, name, number, price) -> None:
        self._name = name
        self._number = number
        self._price = price

    def get_name(self):
        return self._name

    def get_number(self):
        return self._number

    def get_price(self):
        return self._price

    def set_name(self, change):
        self._name = change
        return change

    def set_number(self, change):
        self._number = change
        return change

    def set_price(self, change):
        self._price = change
        return change


lotus = Flower("lotus", 24, 10)
print(lotus.get_number())
print(lotus.set_name("rose"))
