from tkinter import *


root = Tk()
root.title('Window1')
root.geometry('500x200')


def quit():
    exit()


def printText():
    return None


# ----------- The Buttons ---------
label_1 = Label(root, text='Enter some text here: ')
entry_1 = Entry(root)
button_1 = Button(root, text='Print', command=printText)


# ----------- Menu ---------
menu = Menu(root, bg='blue')
root.config(menu=menu)
subMenu = Menu(menu)
menu.add_cascade(label='File', menu=subMenu)
subMenu.add_command(label='Quit', command=quit)

# ------------Toolbar-------


label_1.grid(row=0)
entry_1.grid(row=0, column=1)
button_1.grid(row=0, column=2)

root.mainloop()
