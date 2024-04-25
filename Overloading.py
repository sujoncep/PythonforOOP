a = 3
b = 4
c = a+b
print(c)

l1 = [1, 2, 3, 4, 42]
l2 = [14, 23, 34, 4, 42]
l3 = l1+l2
print(l3)


class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __add__(self, other):
        return self.price + other.price

    def __sub__(self, other):
        return self.price-other.price

    def __mul__(self, other):
        return self.price*other.price


phone1 = Phone('nokia', '1100', 3000)
phone2 = Phone('nokia', '1130', 6000)

print(phone1.__dict__)
print(phone2.__dict__)

print(phone1+phone2)
print(phone1-phone2)
print(phone1*phone2)
