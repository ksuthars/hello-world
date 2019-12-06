#!/usr/dev/python3
from tkinter import *
from tkinter import messagebox
import paho.mqtt.client as mqtt
import time
import csv

class Trip_Button:
    def __init__(self, Name='',i=0, device=''):
        #b = Button(root,text=Name, padx=10, pady=10,command=lambda:self.button_clicked(device,Name))
        b = Button(frame_trip,text=Name, padx=10, pady=10,command=lambda:self.button_clicked(device,Name))
        
        rc = divmod(i,4)
        r,c = rc[0], rc[1]
        b.grid(row=r, column=c)
        #label_Title = Label(root,text=Name)
        #label_Title.grid(row=r, column=c)
        #print("test")
          
    def button_clicked(self, device='',Name=''):

#messagebox.showinfo("Trip",device+"\n"+Name)
        publish_msg(device,Name)
        
def on_log(client, userdata, level, buf):
    print("log: "+buf)

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Connected OK")
    else:
        print("Bad connection, returned code is ", rc)

def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected with result code " + str(rc))

def on_message(client, userdata, msg):
    print("On Messaged............")
    topic = msg.topic
    m_decode = str(msg.payload.decode("utf-8"))
    print("Message received: ", m_decode)

def button_click(device, s):
    publish_msg(device,s)
    #messagebox.showinfo("Info",device+"\n"+s+" Success.")
    return

route = []
with open('routes.csv','r') as f:
    routereader = csv.reader(f)
    route = list(routereader)

def publish_msg(device, message):
    broker = "127.0.0.1"
    client = mqtt.Client(device)
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_log = on_log
    client.on_message = on_message
    print("Connecting to broker ",broker)
    client.connect(broker)
    client.loop_start()
    client.publish(device+"/trip_detail",message)
    #time.sleep(5)
    client.loop_stop()
    print("Disconnecting....")
    client.disconnect()
    
    
bus = route[0][0]
device = route[0][1]

#client.subscribe(device+"/trip_detail")
#time.sleep(30)

root = Tk()
root.geometry('1024x600')

#Test Frame
root.title("Welcome To LIFT System")

frame_name=Frame(root,height=150,width=950,relief=RAISED,bd=8,bg="green")
frame_trip=Frame(root,height=150,width=950,relief=RAISED,bd=8,bg="gray")

label_Bus =Label(frame_name, text="Bus Name")
label_Device =Label(frame_name, text="Device Name")
label_DateTime =Label(frame_name, text="DateTime")
#Triptitle=Label(frame_name, text=txtRoute[0][2])
Triptitle=Label(frame_name, text="Bus Route : GTBC to MainGate")

Tripinfo=Label(frame_trip, text="Trip Information")

entry_Bus =Entry(frame_name)
entry_Device =Entry(frame_name)
entry_DateTime =Entry(frame_name)

Triptitle.grid(columnspan=5,row=0)
Tripinfo.grid(columnspan=5,row=0)

label_Bus.grid(column=0,row=1)
label_Device.grid(column=2,row=1)
label_DateTime.grid(column=4,row=1)

entry_Bus.grid(column=1,row=1)
entry_Device.grid(column=3,row=1)
entry_DateTime.grid(column=5,row=1)
#label_test =Label()
#label_test.grid(row=5,column=0)

trips = []
with open('trips.csv','r') as f:
    tripreader = csv.reader(f)
    trips = list(tripreader)

button = []
txtTrip = []
txtRoute = []
for i in range(len(trips)):
    txtTrip = trips[i][1]
    txtRoute =trips[i][2]
    #button.append(Button(root,text=txtTrip, padx=60, pady=30,command=lambda:button_click(device,txtTrip)))
    Trip_Button(txtTrip,i,device)
   # b = Button(frame_trip,text=Name, padx=10, pady=10,command=lambda:self.button_clicked(device,Name))
    #    rc = divmod(i,4)
     #   r,c = rc[0], rc[1]
      #  b.grid(row=r, column=c)
    
    
#for i in range(len(trips)):
#    button[i].command=lambda:button_click(device,txtTrip))
#    button[i].on_click(on_button_clicked(txtTrip[i]))


# next set of grid
#bar = Progressbar(window,length=200,style='black.Horizontal.TProgressbar')
#bar['value'] = 70
#bar.grid(columnspan=5,row=2)
#frame_name=Frame(root,height=150,width=950,relief=RAISED,bd=8,bg="white")
#frame_name=Frame(root,height=150,width=950,relief=RAISED,bd=8)
frame_name.grid(column=0,row=0)
frame_trip.grid(column=0,row=2)



#e = Entry(root, width=10)

root.mainloop()
