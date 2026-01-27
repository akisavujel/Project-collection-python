import tkinter as tk #Import the tkinter library for GUI
from time import strftime #Import strftime for date and time

root = tk.Tk()
root.title("Digital Clock")

def time():
    string = strftime('%H:%M:%S %p \n %D') #Format of date and time
    label.config(text = string)
    label.after(1000,time) #Update time every second

#GUI for displaying date and time
label = tk.Label(root, font = ('calibri', 50, 'bold'), background = 'pink', foreground='black')
label.pack(anchor='center') #Keep label in center

time() #Call time function

root.mainloop() #Start loop
