from tkinter import *


top = Tk() 
top.geometry("450x300") 

def ful_cost():
    milk_cost = int(milk_amount.get()) * 1.23
    cheese_cost = int(cheese_amount.get()) * 5.23
    eggs_cost = int(eggs_amount.get()) * 1.23
    full_cost = milk_cost + cheese_cost + eggs_cost
    tax_cost = full_cost * 1.06
    print (tax_cost)

milk = Label(top,text='Milk 1.23$').grid(row=1,column=1)
cheese = Label(top,text='Pack Cheese 5.32$').grid(row=2,column=1)
eggs = Label(top,text="Eggs 3.52$").grid(row=3,column=1)

milk_amount = Entry(top,text= 'Milk')
milk_amount.grid(row=1,column=2)
cheese_amount = Entry(top,text= 'Cheese')
cheese_amount.grid(row=2,column=2)
eggs_amount = Entry(top,text= 'Eggs')
eggs_amount.grid(row=3,column=2)

totile = Button(top,text='full cost', command=ful_cost ).grid(row=4,column= 2)

top.mainloop()  
