from tkinter import *

''' 
library of conversion

1 meter = 39.37 inches
1 meter = 3.28 foot
1 foot = 12 inches  
'''

App = Tk()
App.title('Length converter')
App.geometry('400x300')

scales = ['Foot','Inches','Meters']  # a list of the length types

_from = StringVar() #converst from to a variable that can be edited or called
from_menu = OptionMenu(App , _from, *scales)  #here the _from variable extract the variable from the options in the scales list
from_menu.grid( row = 0 , column = 1 , pady=5)

lbl = Label(App, text = 'Convert to ') # a basic message placed in between 'from' and 'to'
lbl.grid(row=0,column=2 , pady=5)

to_= StringVar() #converts 'to' to a variable that can be edited or called
to_menu = OptionMenu(App , to_, *scales) #dropdown button created with the 'scales' table
to_menu.grid(row = 0 , column = 3, pady=5)

numL = Label(App,text = 'Enter your length')
numL.grid(row = 1 , column = 0,columnspan=2, pady=5,)

numE = Entry(App) #a box to input a number and store it in the numE variable
numE.grid(row = 1 , column = 2 , pady=5)

def Converter():
    From = _from.get() #the selected option in from is stored to 'From' variable
    To = to_.get() #the selected option in to_ is stored to 'To' variable
    num= int(numE.get()) #the integer entered in teh line 29 is stored in 'num' variable and is converted it to an int form here

    # if elif code blocks for each possible combination and the calculation to be held once one of them is met is written below

    if From == 'Meters' and To == 'Inches':
        convrt_num = num * 39.37
    elif From == 'Meters' and To == 'Foot':
        convrt_num = num * 3.28
    elif From == 'Foot' and To == 'Inches':
        convrt_num = num * 12
    elif From == 'Inches' and To == 'Meters':
        convrt_num = num / 39.39
    elif From == 'Foot' and To == 'Meters':
        convrt_num = num / 3.28
    elif From == 'Inches' and To == 'Foot':
        convrt_num = num / 12
    else:
        convrt_num = num

    #once the code executes one of the if's, below the answer is set to be printed out

    numL = Label(App, text = round(convrt_num,2), width=5)
    numL.grid(row=1 , column=3, pady=5,columnspan=2)

convtB=Button(App,text='convert',command=Converter) #this is the button to run the converter function once lenght types are entered and an integer is entered
convtB.grid(row=2 , column=0, pady=5,columnspan=2)

App.mainloop()


