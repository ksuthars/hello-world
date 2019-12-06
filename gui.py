from tkinter import *
import csv

def button_add():
    return

route = []
with open('routes.csv','r') as f:
    routereader = csv.reader(f)
    route = list(routereader)

bus = route[0][0]
device = route[0][1]

root = Tk()
root.geometry('1024x600')

trips = []
with open('trips.csv','r') as f:
    tripreader = csv.reader(f)
    trips = list(tripreader)

button = []

for i in range(len(trips)-1):
    txtTrip = trips[i][1]
    button.append(Button(root,text=txtTrip, padx=60, pady=30, command=button_add))
    rc = divmod(i,4)
    r,c = rc[0], rc[1]
    button[i].grid(row=r, column=c)

e = Entry(root, width=10)

root.mainloop()
