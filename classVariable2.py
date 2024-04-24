# extra attribute adding

# class Laptop:
#     def __init__(self, model, price):
#         self.model = model
#         self.price = price


# tuf = Laptop('f15', 100000)
# tufDash = Laptop('f16', 20000)

# print(tuf.__dict__)

# tuf.wifi = 'yes'
# print(tuf.__dict__)


# class issue

class Phone:
    def __init__(self, brand, modelName, price):
        self.brand = brand
        self.modelName = modelName
        self.price = max(price, 0)
        # if price>0:
        #     self.price= price
        # else:
        #     self.price=0

    def completeSpecification(self):
        return f"the brand is {self.brand} and model is {self.modelName} and price is {self.price} "


phone1 = Phone('nokia', '1100', 5000)
phone2 = Phone('iphone', '12pm', 10000)

print(phone1.completeSpecification())
phone1.price = 1000
print(phone1.completeSpecification())
phone1.price = -500
print(phone1.completeSpecification())
