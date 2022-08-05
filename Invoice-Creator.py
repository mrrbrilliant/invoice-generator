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


# Create document
pdf = Document()

# Add page
page = Page()
pdf.add_page(page)
page_layout = SingleColumnLayout(page)
page_layout.vertical_margin = page.get_page_info().get_height() * Decimal(0.02)
page_layout.add(    
        Image(        
        "https://img.freepik.com/premium-vector/cute-white-cat-cartoon-vector-illustration_42750-808.jpg?w=2000",        
        width=Decimal(128),        
        height=Decimal(128),    
        ))
def _build_invoice_information(items):    
    table_001 = Table(number_of_rows=15, number_of_columns=4)  
    for h in ["PRODUCT", "QTY", "UNIT PRICE", "AMOUNT"]:  
        table_001.add(  
            TableCell(  
                Paragraph(h, font_color=X11Color("White")),  
                background_color=HexColor("016934"),  
            )  
        )  
    
    odd_color = HexColor("BBBBBB")  
    even_color = HexColor("FFFFFF")  
    total = 0
    for row_number, item in enumerate(items):  
        total += item[1] * item[2]
        c = even_color if row_number % 2 == 0 else odd_color  
        table_001.add(TableCell(Paragraph(item[0]), background_color=c))  
        table_001.add(TableCell(Paragraph(str(item[1])), background_color=c))  
        table_001.add(TableCell(Paragraph("$ " + str(item[2])), background_color=c))  
        table_001.add(TableCell(Paragraph("$ " + str(item[1] * item[2])), background_color=c))  
        

	# Optionally add some empty rows to have a fixed number of rows for styling purposes
    for row_number in range(3, 10):  
        c = even_color if row_number % 2 == 0 else odd_color  
        for _ in range(0, 4):  
            table_001.add(TableCell(Paragraph(" "), background_color=c))   
    table_001.add(TableCell(Paragraph("Total", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT  ), col_span=3,))  
    table_001.add(TableCell(Paragraph("$" + str(total), horizontal_alignment=Alignment.RIGHT)))  
    table_001.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))  
    table_001.no_borders()  
    return table_001
    
class Store:
    def __init__(self,window):
        self.win=window
        self.items = []
        self.categories=["Phone","Laptop","Shirt","Jeans"]

        self.kurti=["Phone1","Phone2","Phone3","Phone4"]
        self.legis=["Laptop1","Laptop2","Laptop3","Laptop4"]
        self.shirt=["Shirt1","Shirt2","Shirt3","Shirt4"]
        self.jeans=["Jeans1","Jeans2","Jeans3","Jeans4"]

        self.price=IntVar()
        self.qty=IntVar()

        self.tlist=[]

        self.win.geometry("1350x645+0+0")
        space=" "
        self.win.title(space*200+"PC Store")
        heading=Label(self.win,text="Welcome to Cat Store",background="gray",fg="white",font=("Goudy Stout",15))
        heading.pack(fill=X,ipady=10)

        main_frame=Frame(self.win,background="yellow")
        main_frame.pack(fill="both",expand=1)


        form_frame=LabelFrame(main_frame,height=500,pady=100,padx=60,width=550,background="blue",text="Product Details",font=("Elephant",15))
        form_frame.place(x=0,y=0)

        table_frame=LabelFrame(main_frame,height=500,width=1000,background="white",text="Bill Details",font=("Elephant",15))
        table_frame.place(x=550,y=0)

        button_frame=LabelFrame(main_frame,height=100,width=1370,background="dark blue",text="Click Here",font=("Elephant",15))
        button_frame.place(x=0,y=500)

        #Product Details
        Product_Cat=Label(form_frame,text="Category",font=("times new roman",15))
        Product_Cat.place(x=20,y=0,width=120)
        self.categories.insert(0,"Select Category")
        self.Product_Cat_List=ttk.Combobox(form_frame,font=("times new roman",15),values=self.categories)
        self.Product_Cat_List.current(0)
        self.Product_Cat_List.place(x=170,y=0,width=200)

        self.Product_Cat_List.bind('<<ComboboxSelected>>',self.cat)

        Product_Sub=Label(form_frame,text="Sub Category",font=("times new roman",15))
        Product_Sub.place(x=20,y=50,width=120)
        self.Product_Sub_List=ttk.Combobox(form_frame,font=("times new roman",15))
        self.Product_Sub_List.place(x=170,y=50,width=200)

        Product_Rate_lbl=Label(form_frame,text="Price",font=("times new roman",15))
        Product_Rate_lbl.place(x=20,y=100,width=120)
        Product_Rate_txt=Entry(form_frame,font=("times new roman",15),textvariable=self.price)
        Product_Rate_txt.place(x=170,y=100,width=200)

        Product_Qty_lbl=Label(form_frame,text="Quantity",font=("times new roman",15))
        Product_Qty_lbl.place(x=20,y=150,width=120)
        Product_Qty_txt=Entry(form_frame,font=("times new roman",15),textvariable=self.qty)
        Product_Qty_txt.place(x=170,y=150,width=200)

        #Billing Area
        scrolly=Scrollbar(table_frame,orient=VERTICAL)
        self.billarea=Text(table_frame,yscrollcommand=scrolly.set,font=("times new roman",15),fg="blue")
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.billarea.yview)
        self.billarea.pack(fill=BOTH,expand=1)

        #Button
        self.Add_Item_Btn=Button(button_frame,text="Add Item",font=("times new roman",15),command=self.addItem)
        self.Add_Item_Btn.place(x=50,y=0,width=200)

        self.Calc_Bill_Btn=Button(button_frame,text="Calculate Bill",font=("times new roman",15),command=self.makeBill)
        self.Calc_Bill_Btn.place(x=300,y=0,width=200)

        self.Print_Btn=Button(button_frame,text="Print",font=("times new roman",15),command=self.print_bill)
        self.Print_Btn.place(x=550,y=0,width=200)

        self.Reset_Btn=Button(button_frame,text="Reset",font=("times new roman",15),command=self.reset)
        self.Reset_Btn.place(x=800,y=0,width=200)

        self.Exit_Btn=Button(button_frame,text="Exit",font=("times new roman",15),command=self.quit)
        self.Exit_Btn.place(x=1050,y=0,width=200)

        self.heading()



    def cat(self,e=' '):
        if self.Product_Cat_List.get()=="Phone":
            self.Product_Sub_List.config(values=self.kurti)
            self.Product_Sub_List.current(0)
        elif self.Product_Cat_List.get()=="Laptop":
            self.Product_Sub_List.config(values=self.legis)
            self.Product_Sub_List.current(0)
        elif self.Product_Cat_List.get()=="Shirt":
            self.Product_Sub_List.config(values=self.shirt)
            self.Product_Sub_List.current(0)
        elif self.Product_Cat_List.get()=="Jeans":
            self.Product_Sub_List.config(values=self.jeans)
            self.Product_Sub_List.current(0)

    def addItem(self):
        r=self.price.get()
        q=self.qty.get()
        t=r*q
        self.tlist.append(t)
        print(self.tlist)
        self.billarea.insert(END,f'\n {self.Product_Sub_List.get()}\t\t {r} \t {q} \t {t}')
        self.items.append((self.Product_Sub_List.get(), r, q))
    def makeBill(self):
        space=" "
        total=sum(self.tlist)
        self.billarea.insert(END,"\n ++++++++++++++++++++++++++++++++++++++++++++++++")
        self.billarea.insert(END,f'\n Total={space*50} {total}')
            
   
    def print_bill(self):
        page_layout.add(_build_invoice_information(self.items))  
            
        # Empty paragraph for spacing  
        page_layout.add(Paragraph(" "))

        with open("output.pdf", "wb") as pdf_file_handle:
            PDF.dumps(pdf_file_handle, pdf)

    def reset(self):
        self.billarea.delete(1.0,END)
        self.heading()

    def quit(self):
        win.destroy()

    def heading(self):
        self.billarea.delete(1.0,END)
        self.billarea.insert(END,"\t\t\t\t CAT Store ")
        self.billarea.insert(END,"\n\t_______________________________________________________________")
        self.billarea.insert(END,f'\n Product Name \t Price \t Quantity \t\t Total')


if __name__=='__main__':
    win=Tk()
    app=Store(win)
    win.mainloop()