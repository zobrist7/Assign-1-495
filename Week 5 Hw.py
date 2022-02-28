from tkinter import * #importing GUI hub package
from datetime import date #importing the current date package

def calculator(): #defining the new calculations function
   global result #geting the result of function
   result = str(entry.get()) # the input string
   today = date.today() #current date
   dob_data = result.split("/") #splits each piece of data with a "/"
   date1 = int(dob_data[0]) #sets date in days to be first
   month = int(dob_data[1]) #sets date in months to be second
   year = int(dob_data[2]) #sets year third
   dob = date(year,month,date1) #date of birth allowance setup
   numberOfDays = (today - dob).days #current date minus the date of birth
   age = numberOfDays // 365 #allows calculation of age in years
   label=Label(root, text="Your age is " +str(age)) #Adds spice of string so not just numerical value
   label.pack() #pack that allows to run

root = Tk() #connects tkinter to the root variable
root.title('Age Calculator!') #adds a title to program
root.geometry("300x300") #size of input box
entry = Entry(root) #allows input to connect to function
entry.pack() #allows funciton to work

button = Button(root, text="Age", command=calculator, bg='blue', fg='white') #created a button with "age" and colored button
button.pack() #thing that makes button work
root.mainloop() #goes until executed

#Full source
#https://likegeeks.com/python-gui-examples-tkinter-tutorial/
#added color to the button and a title to program