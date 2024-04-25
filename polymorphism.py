
class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    @staticmethod
    def makeACall(phoneNumber):
        print(f"calling {phoneNumber}.....")

    def fullName(self):
        print(f"This is {self.brand} {self.model} and this is a phone")

    def __add__(self, other):
        return f"phone1 model is {self.model}" + f" phone2 model is {other.model}"


class SmartPhone(Phone):
    def __init__(self, brand, model, price, ram, memory, camera):
        Phone.__init__(self, brand, model, price)
        # super.__init__(brand, model, price)
        self.ram = ram
        self.memory = memory
        self.camera = camera

    def fullName(self):
        print(f"This is {self.brand} {self.model} and this is a smartphone")

    def __add__(self, other):
        return f"smartphone1 ram is {self.ram}" + f" smartphone2 ram is {other.ram}"


class IPhone(SmartPhone):
    def __init__(self, brand, model, price, ram, memory, camera, forntCamera):
        SmartPhone.__init__(self, brand, model, price, ram, memory, camera)
        self.forntCamera = forntCamera

    def fullName(self):
        print(f"This is {self.brand} {self.model} and this is a Iphone")

    def __add__(self, other):
        return f"iphone1 fornt camera is {self.forntCamera}" + f" iphone2 fornt camera is {other.forntCamera}"


iphone1 = IPhone('iphone', '12pm', 5000, '8gb', '128gb', '20mp', '8mp')
iphone2 = IPhone('iphone', '13pm', 7000, '12gb', '256gb', '20mp', '8mp')

smartphone1 = SmartPhone('nokia', '1120', 4000, '6gb', '228gb', '10mp')
smartphone2 = SmartPhone('nokia', '1100', 5000, '8gb', '128gb', '20mp')

phone1 = Phone('nokia', '1100', 5000)
phone2 = Phone('nokia', '1130', 7000)

print(phone1+phone2)
print(iphone1+iphone2)
print(smartphone1+smartphone2)
