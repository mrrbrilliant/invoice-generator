from classes.invoice import Invoice
# from classes.customer import Customer
from classes.product import Product
from classes.invoice_entry import InvoiceEntry

product_1 = Product("Iphone 13", "description", None, "consummer electronic", "mobile phone", 999)
product_2 = Product("Iphone 13 Pro", "description", None, "consummer electronic", "mobile phone", 1299)
product_3 = Product("Iphone 13 Pro Max", "description", None, "consummer electronic", "mobile phone", 1599)

print(str(product_1))
print(repr(product_2))

e1=InvoiceEntry.from_product(product_1, 2);
e2=InvoiceEntry.from_product(product_2, 1);
inv=Invoice("001","brilliant",[e1]);
inv.add_entry(e2)
inv.remove_entry(e2)

print(repr(e1))
print(e1.total())
print(repr(inv))
print(inv.sub_total)
print(inv.vat_total)
print(inv.grand_total)