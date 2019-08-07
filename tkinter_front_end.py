# we import everything from tkinter
# oopsql is our python file that manages all SQL database manipulations
from tkinter import *
from sqlite_back_end import Database


database=Database("inventory.db")


# this code is related to window where we see all the items in our directory
# it is connected to created list1 tkinter variable

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])

# self explanatory functions that we use in order to modify our data base
# selected_tuple[0] is ID of our item and not anything we add ourselfs
# ID is an integer, and out functions rely on getting that ID in order to
# make operations with correct data
# name_text.get() and ect are items that we put in our data fields
def delete_command():
    database.delete(selected_tuple[0])

def update_command():
    database.update(selected_tuple[0],(name_text.get(), location_text.get(),quantity_text.get(),id_name_text.get()))

# use list1.delete(0,END) so that the data is not being copied from over again
def view_command():
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0,END)
    for row in database.search(name_text.get(), location_text.get(),quantity_text.get(),id_name_text.get()):
        list1.insert(END,row)

def add_command():
    database.insert(name_text.get(), location_text.get(),quantity_text.get(),id_name_text.get())
    list1.delete(0,END)
    list1.insert(END, (name_text.get(), location_text.get(),quantity_text.get(),id_name_text.get()))


# our tkinter items
#Label item is used for making a 'label' or text on our GUI
window =Tk()
l1= Label(window, text= 'Name')
l1. grid(row=0, column =0)
l1= Label(window, text= 'Location')
l1. grid(row=0, column =2)
l1= Label(window, text= 'Quantity')
l1. grid(row=1, column =0)
l1= Label(window, text= 'ID')
l1. grid(row=1, column =2)

# Entry is text field where we can input our information
# use StringVar() to make our input a string
name_text=StringVar()
e1=Entry(window, textvariable= name_text)
e1.grid(row=0, column =1)

# use StringVar() to make our input a string
location_text=StringVar()
e2=Entry(window, textvariable= location_text)
e2.grid(row=0, column =3)

quantity_text=StringVar()
e3=Entry(window, textvariable= quantity_text)
e3.grid(row=1, column =1)

id_name_text=StringVar()
e4=Entry(window, textvariable= id_name_text)
e4.grid(row=1, column =3)


list1=Listbox(window, height=6, width=36)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2, column =2, rowspan=6)

# allows us to scroll in the window with all sets
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
# selects items that we clicked from the window
list1.bind('<<ListboxSelect>>',get_selected_row)

# command = something is used to call a function when that button is pressed
# we don't need () when we use command
# text is how we call our buttons
b1=Button(window,text="View all", width = 15,command=view_command)
b1.grid(row=2, column =3)

b2=Button(window,text="Search Entry", width = 15,command=search_command)
b2.grid(row=3, column =3)

b3=Button(window,text="Add Entry", width = 15, command=add_command)
b3.grid(row=4, column =3)

b4=Button(window,text="Update Selected", width = 15, command=update_command)
b4.grid(row=5, column =3)

b5=Button(window,text="Delete Selected", width = 15, command=delete_command)
b5.grid(row=6, column =3)

# window.destroy closes that application
b6=Button(window,text="Close", width = 15, command=window.destroy)
b6.grid(row=7, column =3)

window.mainloop()






