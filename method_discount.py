class Product:
    def __init__(self, productName, productPrice):
        self.productName = productName
        self.productPrice = productPrice

    def discount(self, percentage):
        discountAmount = (self.productPrice/100)*percentage
        finalPrice = self.productPrice-discountAmount
        return finalPrice

    def display(self, price):
        print("Congratulation! your laptop price is now " + str(price))


laptop = Product("asus", 100000)
laptop.discount(5)
laptop.display(laptop.discount(10))
