from tkinter import *
import csv

def text_update(animal):
    text.delete(0,END)
    text.delete(0,animal)
    
root = Tk()

text = Entry(root, width=35, bg='yellow')
text.grid(row=0, column=0,columnspan=5)

# btn_dict= {}

#col=0
#words = ["Dog","Cat","Pig","Cow","Rat"]
#print(words)

#for animal in words:
 #   action = lambda x= animal: text_update(x)
  #  btn_dict[animal] =Button(root,text=animal, command=action)
   # btn_dict[animal].grid(row=1,column=col,pady=5)
    #col +=1
#print(animal)

Out = open('trips.csv','r')
tripreader = csv.reader(Out)
tripreader=[row for row in tripreader]
tripreader=[[row[1],row[2],row[3],row[4]] for row in tripreader]
#print (row)
Out.close
print (tripreader)

button = []
txtTrip = []
txtAvail = []

for TripBut in tripreader:
    action = lambda:button_click(device,txtTrip)
    btn_dict[TripBut] =Button(frame_trip,text=txtTrip[1], command=action)
    rc = divmod(col,4)
    r,c = rc[0], rc[1]
   
root.mainloop()