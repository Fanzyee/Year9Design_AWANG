# Importing tkinter module into python so we can use
from tkinter import *                             
# Tk() makes a window
master = Tk()

def return_entry(en):
    content = entry.get()
    
    if(content != ""):
        print(content)
        
        entry.delete(0, END)
	
Label(master, text="Input: ").grid(row=0, sticky=W)

entry = Entry(master)
entry.grid(row=0, column=1)

# Connect the entry to the return button
entry.bind('<Return>', return_entry)

# mainloop is a function that allows the window to stay open. It REPEATS the code
mainloop()