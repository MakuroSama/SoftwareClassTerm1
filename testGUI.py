from tkinter import *
from tkinter import ttk

def calculate():
    result = 0
    EntryTotal.delete(0,END)
    
    num1 = Entry1.get()
    num2 = Entry2.get()
    if str(v.get()) == "1":
        result = int(num1) + int(num2)
        EntryTotal.insert(0,str(result))
    elif str(v.get()) == "2":
        result = int(num1) - int(num2)
        EntryTotal.insert(0,str(result))
    elif str(v.get()) == "3":
        result = int(num1) * int(num2)
        EntryTotal.insert(0,str(result))
    elif str(v.get()) == "4":
        result = int(num1) / int(num2)
        EntryTotal.insert(0,str(result))

def clear():
    EntryTotal.delete(0,END)
    Entry1.delete(0,END)
    Entry2.delete(0,END)
mainFrm = Tk()
mainFrm.title("System register")

LabelFrame1 = ttk.LabelFrame(mainFrm, text="Calculation System", labelanchor="n")
LabelFrame1.pack(side="left", padx=10, pady=10)

Label1 = ttk.Label(LabelFrame1, text="Number 1")
Label2 = ttk.Label(LabelFrame1, text="Number2")
LabelTotal = ttk.Label(LabelFrame1, text="total")

Label1.grid(column=0,row=2,pady=5,sticky="NE")
Label2.grid(column=0,row=3,pady=5,sticky="NE")
LabelTotal.grid(column=0,row=4,pady=5,sticky="NE")

Entry1 = ttk.Entry(LabelFrame1,width=25)
Entry1.grid(column=1,row=2,sticky="NE")
Entry2 = ttk.Entry(LabelFrame1,width=25)
Entry2.grid(column=1,row=3,sticky="NE")
EntryTotal = ttk.Entry(LabelFrame1,width=25)
EntryTotal.grid(column=1,row=4,sticky="NE")

ButtonClick = ttk.Button(LabelFrame1, text="Cal",width=10,command= calculate)
ButtonClear = ttk.Button(LabelFrame1, text="Clear",width=10,command= clear)

ButtonClick.grid(column=0, row=5, padx=10, sticky="NE")
ButtonClear.grid(column=1, row=5, padx=10, sticky="NE")

LabelFrame2 = ttk.LabelFrame(mainFrm, text="calculate", labelanchor="n")
LabelFrame2.pack(padx=10,pady=10)

v = StringVar(LabelFrame2,"1")
values = {
    "plus" : "1",
    "minus" : "2",
    "multiply" : "3",
    "divide" : "4"
}

for(text, valuess) in values.items():
    Radiobutton(LabelFrame2,text=text,variable=v,value=valuess).pack(side=TOP, ipady=4)

mainFrm.mainloop()