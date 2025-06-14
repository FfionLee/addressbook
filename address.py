from tkinter import *
from tkinter.filedialog import *

ui=Tk()
ui.config(background='SteelBlue')
ui.geometry('500x500')

addressbook={}

def addfun():
    key=namin.get()
    addressbook[key]=(addressin.get(),phonein.get(),emailin.get(),bdayin.get())
    list.insert(END,key)
    clearall()

def clearall():
    namin.delete(0,END)
    addressin.delete(0,END)
    phonein.delete(0,END)
    emailin.delete(0,END)
    bdayin.delete(0,END)

def edit():
    global addressbook
    clearall()
    index=list.curselection()
    key=list.get(index)
    namin.insert(0,key)
    addressin.insert(0,addressbook[key][0])
    phonein.insert(0,addressbook[key][1])
    emailin.insert(0,addressbook[key][2])
    bdayin.insert(0,addressbook[key][3]) 

def display(event):
    global addressbook
    window=Toplevel(ui)
    details=Label(window)
    index=list.curselection()
    key=list.get(index)
    content='Name: '+key+'\n'+'Address: '+addressbook[key][0]+'\n'+'Phone No.: '+addressbook[key][1]+'\n'+'Email: '+addressbook[key][2]+'\n'+'Birthday: '+addressbook[key][3]
    details.config(text=content)
    details.pack()

def delete():
    index=list.curselection()
    key=list.get(index)
    list.delete(index)
    del addressbook[key]
    print(addressbook)

def save():
    global addressbook
    f=asksaveasfile(defaultextension='txt')
    print(addressbook,file=f)

title=Label(ui,text='Address Book',bg='SteelBlue',fg='white',font='TkDefaultFont 20')
title.pack(pady=20)

openb=Button(ui,text='OPEN')
openb.pack()

frame=Frame(ui,bg='SteelBlue')
frame.place(x=300,y=120)

nam=Label(frame,text='Name: ',bg='SteelBlue',fg='white')
nam.grid(column=0,row=0)
namin=Entry(frame)
namin.grid(column=1,row=0)

address=Label(frame,text='Address: ',bg='SteelBlue',fg='white')
address.grid(column=0,row=1,pady=10)
addressin=Entry(frame)
addressin.grid(column=1,row=1)

phone=Label(frame,text='Phone No.: ',bg='SteelBlue',fg='white')
phone.grid(column=0,row=2)
phonein=Entry(frame)
phonein.grid(column=1,row=2)

email=Label(frame,text='Email: ',bg='SteelBlue',fg='white')
email.grid(column=0,row=3,pady=10)
emailin=Entry(frame)
emailin.grid(column=1,row=3)

bday=Label(frame,text='Birthday: ',bg='SteelBlue',fg='white')
bday.grid(column=0,row=4)
bdayin=Entry(frame)
bdayin.grid(column=1,row=4)

list=Listbox(ui,width=40)
list.place(x=10,y=120)
list.bind('<<ListboxSelect>>',display)

editb=Button(ui,text='EDIT',command=edit)
editb.place(x=50,y=300)

delb=Button(ui,text='DELETE',command=delete)
delb.place(x=150,y=300)

addb=Button(ui,text='ADD',command=addfun)
addb.place(x=350,y=300)

saveb=Button(ui,text='SAVE',command=save)
saveb.place(x=450,y=300)

ui.mainloop()
