# Clock

from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('Clock')
root.resizable(width=False, height=False)

lbl = Label(root, font=('calibri', 40, 'bold'),
            background='#f7f4e9', foreground='#1d1d2c')

def time():
    mx = strftime('%H:%M:%S %p')
    lbl.config(text=mx)
    lbl.after(1000, time)

lbl.pack(anchor='center')
time()
mainloop()

# Moein Heshmati