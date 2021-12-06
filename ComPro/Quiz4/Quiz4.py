class Car:
    def __init__(self, brand='_', model='_', price=0):
        self.__brand = brand
        self.__model = model
        self.__price = price

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    def __str__(self):
        return "Brand: {0} , Model: {1} , Price: {2}".format(self.__brand, self.__model, self.__price)


def compare(car1, car2):
    print(car1)
    print(car2)


print("Level 1")
car1 = Car()
print(car1)
car1.brand = "Toyota"
print(car1)
car1.model = "Vios"
car1.price = 500000
print(car1)

car2 = Car("BMW", "X3", 3500000)
print(car2)
car2.price = 2000000
print(car2)

print("Level 2")
car1 = Car("Nissan", "Tiida", 450000)
car2 = Car("Totoya", "Vios", 400000)
car3 = Car("BMW", "X3", 3400000)
compare(car3, car1)
compare(car1, car2)
