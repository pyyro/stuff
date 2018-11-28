from tkinter import *

root = Tk()


def leftClick(event):
    print('Left')


def middleClick(event):
    print('Middle')


def rightClick(event):
    print('Right')


button1 = Button(root, text='Click Me!')
label1 = Label(root, text='Keep an eye on the console!')
button1.bind('<Button-1>', leftClick)
button1.bind('<Button-2>', middleClick)
button1.bind('<Button-3>', rightClick)


button1.pack()
label1.pack()

root.mainloop()
