from tkinter import *

root = Tk()
root.title('Window with buttons lol')
root.geometry('500x200')
root.resizable(0,0)


topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

buttonLabel = Label(topFrame, text='Type whatever in the box and press Enter.')
buttonLabel.pack(side=TOP)

entry1 = Entry(topFrame)
entry1.pack(side=LEFT)

button1 = Button(topFrame, text='Print') 	  
button1.pack(side=RIGHT)


button2 = Button(bottomFrame, text='Quit') 	  
button2.pack(side=LEFT)


root.mainloop()
