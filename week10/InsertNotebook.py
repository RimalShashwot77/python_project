# pip install tk
from tkinter import Tk # Window
from tkinter import Label # Label
from tkinter import Entry # Entry
from tkinter import Button # Button
from notebook import NoteBook
from notebookmanager import insert

def save():
    # reading value from entry and send to library/middleware
    nid = int(txtNID.get())
    pages = int(txtPages.get())
    price = float(txtPrice.get())
    nb1 = NoteBook(nid, pages, price)
    result = insert(nb1)
    if(result==True):
        print("Insert successfully")
    else:
        print("Error to insert")

# Declare and initialize
window = Tk() # declare and initialize
window.geometry("250x350") # Resize
window.resizable(False,False) # resizable-> False
window.title("Insert New Record")

lblNID = Label(window, text="NID:")
lblPages = Label(window, text="PAGE:")
lblPrice = Label(window, text="PRICE:")

txtNID = Entry(window,width=20)
txtPages = Entry(window,width=20)
txtPrice = Entry(window,width=20)

btnSave = Button(window,text="SEARCH", command=save) # calling save function
btnClose = Button(window,text="CLOSE")

lblNID.place(x=20, y=10)
txtNID.place(x=100, y=10)

lblPages.place(x=20, y=40)
txtPages.place(x=100, y=40)

lblPrice.place(x=20, y=70)
txtPrice.place(x=100, y=70)

btnSave.place(x=100, y=100)
btnClose.place(x=150, y=100)

window.mainloop()# display

# Resize window