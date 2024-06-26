
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


# phone = Phone('nokia', '1100', 5000)

# phone.makeACall(2441139)
# phone.fullName()


class SmartPhone(Phone):
    def __init__(self, brand, model, price, ram, memory, camera):
        Phone.__init__(self, brand, model, price)
        # super.__init__(brand, model, price)
        self.ram = ram
        self.memory = memory
        self.camera = camera

    def fullName(self):
        print(f"This is {self.brand} {self.model} and this is a smartphone")


# smartphone = SmartPhone('nokia', '1100', 5000, '8gb', '128gb', '20mp')

# smartphone.makeACall(2441139)
# smartphone.fullName()


class IPhone(SmartPhone):
    def __init__(self, brand, model, price, ram, memory, camera, forntCamera):
        SmartPhone.__init__(self, brand, model, price, ram, memory, camera)
        self.forntCamera = forntCamera

    def fullName(self):
        print(f"This is {self.brand} {self.model} and this is a Iphone")


iphone = IPhone('nokia', '1100', 5000, '8gb', '128gb', '20mp', '8mp')
smartphone = SmartPhone('nokia', '1100', 5000, '8gb', '128gb', '20mp')
phone = Phone('nokia', '1100', 5000)

# iphone.fullName()
# smartphone.fullName()
# phone.fullName()

print(isinstance(phone, IPhone))


# in python everything is pulic

# Naming convention
# Dunder methods are used to define behaviors for various built-in operations and functionalities, such as object initialization, comparison, arithmetic operations, attribute access, and more. These methods allow you to customize the behavior of your objects and classes, making them more powerful and flexible.

# __init__: This method is called when an object is created. It is used to initialize the object's attributes.
