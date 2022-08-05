from classes.invoice import Invoice

class Shop:
    customers = []
    invoices = []
    products = []
    sellers = []

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def add_customer(self, customer):
      self.customers.append(customer)

    def remove_customer(self, customer):
      self.customers.remove(customer)

    def add_invoice(self, invoice):
      self.invoices.append(invoice)

    def remove_invoice(self, invoice):
      self.invoices.remove(invoice)

    def add_product(self, product):
      self.products.append(product)

    def remove_product(self, product):
      self.products.remove(product)

    def add_seller(self, seller):
      self.sellers.append(seller)

    def remove_seller(self, seller):
      self.sellers.remove(seller)
    
    @property
    def count_customers(self):
      return len(self.customer)

    @property
    def count_products(self):
      return len(self.products)
    
    @property
    def count_sellers(self):
      return len(self.sellers)

    @property
    def count_invoices(self):
      return len(self.invoices)

    @property
    def revenue(self):
      rev=0
      for inv in self.invoices:
        rev = rev + Invoice.grand_total(inv)
      return rev
