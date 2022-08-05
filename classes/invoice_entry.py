from unicodedata import category
from classes.product import Product

class InvoiceEntry(Product):
    def __init__(self, name,image,category,subcategory,price, quantity):
        super().__init__(name,image,category,subcategory,price)
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity

    @classmethod
    def from_product(cls, product, quantity):
        name = product.name
        image = product.image
        category = product.category
        subcategory = product.subcategory
        price = product.price

        return cls(name,image,category,subcategory,price, quantity)

    def __repr__(self):
        name = self.name
        image = self.image
        category = self.category
        subcategory = self.subcategory
        price = self.price
        quantity = self.quantity
        return "InvoiceEntry('{}','{}','{}','{}','{}','{}')".format(name,image,category,subcategory,price, quantity)

    def __str__(self):
        name = self.name
        image = self.image
        category = self.category
        subcategory = self.subcategory
        price = self.price
        quantity = self.quantity
        return "InvoiceEntry: {},{},{},{},{},{}".format(name,image,category,subcategory,price, quantity)