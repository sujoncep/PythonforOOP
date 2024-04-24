class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    @staticmethod
    def makeACall(phoneNumber):
        print(f"calling {phoneNumber}.....")

    def fullName(self):
        print(f"{self.brand} {self.model}")


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

    # @staticmethod
    # def makeACall(phoneNumber):
    #     print(f"calling {phoneNumber}.....")

    # def fullName(self):
    #     print(f"{self.brand} {self.model}")


# smartphone = SmartPhone('nokia', '1100', 5000, '8gb', '128gb', '20mp')

# smartphone.makeACall(2441139)
# smartphone.fullName()


class IPhone(SmartPhone):
    def __init__(self, brand, model, price, ram, memory, camera, forntCamera):
        SmartPhone.__init__(self, brand, model, price, ram, memory, camera)
        self.forntCamera = forntCamera

    # @staticmethod
    # def makeACall(phoneNumber):
    #     print(f"calling {phoneNumber}.....")

    # def fullName(self):
    #     print(f"{self.brand} {self.model}")


iphone = IPhone('nokia', '1100', 5000, '8gb', '128gb', '20mp', '8mp')

iphone.makeACall(2441139)
iphone.fullName()
