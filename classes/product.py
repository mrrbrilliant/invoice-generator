class Product:
    def __init__(self,name,image,category,subcategory,price):
        self.name = name
        self.image = image
        self.category = category
        self.subcategory = subcategory
        self.price = price

    def __repr__(self):
        return "Product('{}','{}','{}','{}', '{}')".format(self.name, self.image, self.category,self.subcategory,self.price)

    def __str__(self):
        return "Product: {},{},{},{},{}".format(self.name, self.image, self.category,self.subcategory,self.price)
