from classes.invoice_entry import InvoiceEntry

class Invoice:
    discount=0
    vat=0.1
    def __init__(self, id, customer, entries=None):
        self.id = id
        self.customer = customer
        if entries is None:
            self.entries = []
        else:
            self.entries = entries

    @property
    def sub_total(self):
        total=0
        for entry in self.entries:
            total = total + InvoiceEntry.total(entry)
        return total

    @property
    def after_discount(self):
        total=0
        for entry in self.entries:
            total = total + InvoiceEntry.total(entry)
        return total
    @property
    def vat_total(self):
        return (self.sub_total - self.discount) * self.vat

    @property
    def grand_total(self):
        return self.sub_total - self.discount + self.vat_total

    def add_entry(self, entry):
        self.entries.append(entry)

    def remove_entry(self, entry):
        self.entries.remove(entry)

    def clear_entry(self):
        self.entries.clear()

    def __repr__(self):
        return "Invoice('{}','{}','{}')".format(self.id, self.customer,self.entries)

    def __str__(self):
        return "Invoice: {},{},{}".format(self.id, self.customer,self.entries)
