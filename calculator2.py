from tkinter import *
root=Tk()
root.title("GUI Simple Calculator")

entry=Entry(root,width=45,borderwidth=4)
entry.grid(row=0,column=0,columnspan=4)

def click(x):
    current=entry.get()
    entry.delete(0,END)
    entry.insert(END,str(current)+str(x))

def clear():
    entry.delete(0,END)

def sign(x):
    entry.insert(END,x)

def evaluate():
    to_evaluate=entry.get()
    entry.delete(0,END)
    entry.insert(END,eval(to_evaluate))

button_1=Button(root,text='1',padx=40,pady=20,command=lambda: click(1))
button_2=Button(root,text='2',padx=40,pady=20,command=lambda: click(2))
button_3=Button(root,text='3',padx=40,pady=20,command=lambda: click(3))
button_4=Button(root,text='4',padx=40,pady=20,command=lambda: click(4))
button_5=Button(root,text='5',padx=40,pady=20,command=lambda: click(5))
button_6=Button(root,text='6',padx=40,pady=20,command=lambda: click(6))
button_7=Button(root,text='7',padx=40,pady=20,command=lambda: click(7))
button_8=Button(root,text='8',padx=40,pady=20,command=lambda: click(8))
button_9=Button(root,text='9',padx=40,pady=20,command=lambda: click(9))
button_0=Button(root,text='0',padx=40,pady=20,command=lambda: click(0))
button_multiply=Button(root,text="*",padx=40,pady=20,command=lambda:sign('*'))
button_subtract=Button(root,text="-",padx=40,pady=20,command=lambda:sign('-'))
button_add=Button(root,text="+",padx=40,pady=52,command=lambda:sign('+'))
button_divide=Button(root,text="/",padx=40,pady=20,command=lambda:sign('/'))
button_clear=Button(root,text="clear",padx=78,pady=20,command=lambda: clear())
button_equals=Button(root,text=" = ",padx=83,pady=20,command=evaluate)
button_dot=Button(root,text=" .",padx=40,pady=20,command=lambda:sign('.'))

button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_0.grid(row=5,column=0)
button_multiply.grid(row=3,column=4)
button_subtract.grid(row=4,column=4)
button_add.grid(row=5,column=4,rowspan=2)
button_divide.grid(row=2,column=4)
button_clear.grid(row=5,column=1,columnspan=2)
button_equals.grid(row=6,column=1,columnspan=2)
button_dot.grid(row=6,column=0)

root.mainloop()