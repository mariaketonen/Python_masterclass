try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Calculator")
mainWindow.geometry('640x480-8-200') # 640x480-8-200
mainWindow['padx'] = 8

label = tkinter.Label(mainWindow, text="Calculator")
label.grid(row=0, column=0, columnspan=4)

#resultLabel = tkinter.Label(mainWindow, text="Result")
#resultLabel.grid(row=1, column=0, columnspan=5)
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=0, columnspan=5)

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)
mainWindow.columnconfigure(3, weight=1)
mainWindow.columnconfigure(4, weight=1)
mainWindow.columnconfigure(5, weight=1)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=1)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=1)
mainWindow.rowconfigure(4, weight=1)
mainWindow.rowconfigure(5, weight=1)
mainWindow.rowconfigure(6, weight=1)

# buttons
number1Button = tkinter.Button(mainWindow, text="1")
number2Button = tkinter.Button(mainWindow, text="2")
number3Button = tkinter.Button(mainWindow, text="3")
plusButton = tkinter.Button(mainWindow, text="+")
number1Button.grid(row=3, column=0, sticky='e')
number2Button.grid(row=3, column=1, sticky='e')
number3Button.grid(row=3, column=2, sticky='e')
plusButton.grid(row=3, column=3, sticky='e')

number4Button = tkinter.Button(mainWindow, text="4")
number5Button = tkinter.Button(mainWindow, text="5")
number6Button = tkinter.Button(mainWindow, text="6")
minusButton = tkinter.Button(mainWindow, text="-")
number4Button.grid(row=4, column=0, sticky='e')
number5Button.grid(row=4, column=1, sticky='e')
number6Button.grid(row=4, column=2, sticky='e')
minusButton.grid(row=4, column=3, sticky='e')

number7Button = tkinter.Button(mainWindow, text="7")
number8Button = tkinter.Button(mainWindow, text="8")
number9Button = tkinter.Button(mainWindow, text="9")
timesButton = tkinter.Button(mainWindow, text="*")
number7Button.grid(row=5, column=0, sticky='e')
number8Button.grid(row=5, column=1, sticky='e')
number9Button.grid(row=5, column=2, sticky='e')
timesButton.grid(row=5, column=3, sticky='e')

number0Button = tkinter.Button(mainWindow, text="0")
equalButton = tkinter.Button(mainWindow, text="=")
divideButton = tkinter.Button(mainWindow, text="/")
number0Button.grid(row=6, column=0, sticky='e')
equalButton.grid(row=6, column=1, columnspan=2)
divideButton.grid(row=6, column=3, sticky='e')

mainWindow.mainloop()
