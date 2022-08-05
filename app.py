from cProfile import label
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import tempfile
from borb.pdf import Document
from borb.pdf.page.page import Page
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from decimal import Decimal
from borb.pdf.canvas.layout.image.image import Image
from borb.pdf.canvas.layout.table.fixed_column_width_table import FixedColumnWidthTable as Table
from borb.pdf.canvas.layout.table.table import TableCell
from borb.pdf.canvas.color.color import HexColor, X11Color

from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.canvas.layout.layout_element import Alignment
from datetime import datetime
import random
from borb.pdf.pdf import PDF

from classes.invoice import Invoice
from classes.shop import Shop
from classes.invoice_entry import InvoiceEntry
from classes.product import Product

def initial_products(self):
      product_1 = Product("Iphone 13", None, "Consummer Electronic", "Smart phone", 999)
      product_2 = Product("Iphone 13 Pro", None, "Consummer Electronic", "Smart phone", 1299)
      product_3 = Product("Iphone 13 Pro Max", None, "Consummer Electronic", "Smart phone", 1599)

      product_4 = Product("Tesla Model S", None, "Vehicle", "Car", 999)
      product_5 = Product("Tesla Model E", None, "Vehicle", "Car", 1299)
      product_6 = Product("Tesla Model X", None, "Vehicle", "Car", 1599)

      product_7 = Product("Ring", None, "Wearable", "Jewelery", 999)
      product_8 = Product("Ear ring", None, "Wearable", "Jewelery", 1299)
      product_9 = Product("Necklace", None, "Wearable", "Jewelery", 1599)

      self.add_product(product_1)
      self.add_product(product_2)
      self.add_product(product_3)
      self.add_product(product_4)
      self.add_product(product_5)
      self.add_product(product_6)
      self.add_product(product_7)
      self.add_product(product_8)
      self.add_product(product_9)

class Card(Product):
    def __init__(self, product, parent, invoice):

      super().__init__(product.name,product.image,product.category,product.subcategory,product.price)
      self.parent = parent
      self.invoice = invoice

      self.label = Button(self.parent, text=product.name, width=50, command=lambda: self.hanlde_log())
      self.label.pack()

    def hanlde_log(self):
        # data = self.products[i]
        # print(self.name)
        # print(self.price)
        entry = InvoiceEntry(self.name,self.image,self.category,self.subcategory,self.price, 1)
        self.invoice.add_entry(entry)

      

class Store(Shop):

    invoice = Invoice("001", "Niki", None)
    def __init__(self,window):
        super().__init__("Rassa Shop", "Phnom Penh, Cambodia")
        initial_products(self)
        self.win=window
        
        # WINDOW
        self.win.geometry("1350x645+0+0")
        intvar = IntVar(self.win, name ="int")

        print("Value of IntVar()", self.win.getvar(name ="int"))
        # HEADER
        heading=Label(self.win,text=self.name,background="gray",fg="white",font=("Elephant",15))
        heading.pack(fill=X,ipady=10)

        main_frame=Frame(self.win)
        main_frame.pack(fill="both",expand=1)

        form_frame=LabelFrame(main_frame,height=500,pady=100,padx=60,width=550,background="white",text="Product Details",fg="black",font=("Elephant",15))
        form_frame.place(x=0,y=0)

        table_frame=LabelFrame(main_frame,height=500,width=1000,background="white",text="Bill Details",font=("Elephant",15))
        table_frame.place(x=550,y=0)
    
        button_frame=LabelFrame(main_frame,height=100,width=1370,background="white",text="Click Here",font=("Elephant",15))
        button_frame.place(x=0,y=500)

        # Products
        for i, product in  enumerate(self.products):
          Card( product, form_frame, self.invoice)


        self.Add_Item_Btn=Button(button_frame,text="Add Item",font=("times new roman",15))
        self.Add_Item_Btn.place(x=50,y=0,width=200)

        self.Calc_Bill_Btn=Button(button_frame,text="Calculate Bill",font=("times new roman",15))
        self.Calc_Bill_Btn.place(x=300,y=0,width=200)

        self.Print_Btn=Button(button_frame,text="Print",font=("times new roman",15))
        self.Print_Btn.place(x=550,y=0,width=200)

        self.Reset_Btn=Button(button_frame,text="Reset",font=("times new roman",15))
        self.Reset_Btn.place(x=800,y=0,width=200)

        self.Exit_Btn=Button(button_frame,text="Exit",font=("times new roman",15))
        self.Exit_Btn.place(x=1050,y=0,width=200)
        
if __name__=='__main__':
    win=Tk()
    app=Store(win)
    win.mainloop()