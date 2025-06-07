from tkinter import *

ui=Tk()
ui.config(background='SteelBlue')
ui.geometry('500x500')

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

editb=Button(ui,text='EDIT')
editb.place(x=50,y=300)

delb=Button(ui,text='DELETE')
delb.place(x=200,y=300)

ui.mainloop()