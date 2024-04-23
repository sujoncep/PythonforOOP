# create a product class with attribute like name,brand, name, price

class Product:
    def __init__(self, product_name, product_brand, model_name, price):
        self.product_name = product_name
        self.product_brand = product_brand
        self.model_name = model_name
        self.price = price
        self.product_nameWithModel = product_name+' '+model_name


laptop = Product("laptop", "Asus", "Tuf_f15", 100000)
mobile = Product("mobile", "Xaomi", "pocox3", 26000)
print(laptop.model_name)
print(mobile.model_name)
print(laptop.product_nameWithModel)
