from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Binary Search Application")
window.geometry("400x300")

import csv

data = []
with open("data.csv") as csvfile:  # Replace 'data.csv' with your file name
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)  # Append each row to the data list

arr = [x[0] for x in data]  # This is the first column

def binarysearch():
    low = 0
    high = len(arr) - 1
    boolFound = False
    while low <= high and boolFound == False:
        mid = int(low + (high - low) // 2)  # Floor division
        if int(e1.get()) == int(arr[mid]):
            boolFound = True
        elif int(e1.get()) > int(arr[mid]):
            low = mid + 1
        else:
            high = mid - 1
    if boolFound == True:
        lblmessage.config(text="found")
    else:
        lblmessage.config(text="not found")

lblmessage = ttk.Label(window, text="")
lblmessage.pack()

e1 = Entry(window)  # Create an Entry widget for user input
e1.pack()  # Pack the Entry widget

btnSearch = Button(window, text="binary search")  # Create a button
btnSearch.pack()  # Pack the button
btnSearch.config(command=binarysearch)  # Set the command for the button

mainloop()