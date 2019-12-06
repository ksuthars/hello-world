#!/usr/dev/python3
from tkinter import *
from tkinter import messagebox
import paho.mqtt.client as mqtt
import datetime
from datetime import date
import time
import csv
#import mytest

class Trip_Button:

    def __init__(self, Name='',i=0, device=''):
        ##b = Button(root,text=Name, padx=10, pady=10,command=lambda:self.button_clicked(device,Name))
        b = Button(frame_trip,text=Name, padx=55, pady=10,command=lambda:self.button_clicked(device,Name))
        rc = divmod(i,4)
        r,c = rc[0], rc[1]
        b.grid(row=r, column=c)
        TrpName = ''
        
        #print_btn(Name)
        #my_var = StringVar()
        #my_var.set(Name)

    def button_clicked(self, device='',Name=''):
        global Btn_txt
        #frame_trip.state = DISABLED
        #messagebox.showinfo("Trip",device+"\n"+Name)
        #print(Name+"/"+str(datetime.date.today()))
        #txtTrip = []
        #txtAvail = []
        #txtBook = []
        Btn_txt=Name
        print (Btn_txt)
        TrpName = Name+"/"+str(datetime.date.today())
        publish_msg(device,TrpName)
        second_win()
        #frame_trip.visible = false
        #frame_pass.visible = true
        
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
    print(message)
    #client.publish(device+"/"+TrpName+"/"+str(today),message)
    #time.sleep(5)
    client.loop_stop()
    print("Disconnecting....")
    client.disconnect()

        
def on_log(client, userdata, level, buf):
    print("log: "+buf)

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Connected OK")
        #====================newly added
        #client.subscribe("26051D64/101/2019-12-03 18:06:40.632318")
        #====================newly added end
    else:
        print("Bad connection, returned code is ", rc)

def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected with result code " + str(rc))

def on_message(client, userdata, msg):
    print("On Messaged............")
    print (msg.topic + " " + str(msg.qos) + " " + msg.payload.decode("utf-8"))
    toptype=msg.topic.split('/')
    topic = msg.topic
    m_decode = str(msg.payload.decode("utf-8"))
    print("Message received: ", m_decode)
    if msg.payload == "hello":
        print("Received message, do something")
    else:
        print("Do something else")

def button_click(device, s):
    publish_msg(device,s)
    #messagebox.showinfo("Info",device+"\n"+s+" Success.")
    return
#==================================Passenger/Seat Info ===================================
def second_win():
    window=Tk()
    window.title("LIFT Passenger Details")
    window.geometry('660x200')
    window.config(bg='powder blue')
    print(Btn_txt)
    #Triptitle_1=Label(window, text=busRName,justify=CENTER,padx=250, pady=5,font=('arial',15,'bold'),bd=1,bg='powder blue',fg='green')
    Triptitle_1=Label(window, text=busRName,justify=CENTER,padx=20, pady=1,font=('arial',15,'bold'),bd=1,bg='powder blue',fg='green')
    TripVac_1=Label(window, text="Available Seats: 5 ",justify=CENTER,padx=5, pady=1,font=('arial',15,'bold'),bd=1,bg='powder blue',fg='green')    
    label_Bus_1 =Label(window, text="Bus Name",font=('arial',10,'bold'),bd=12,bg='gray',fg='white')
    label_Device_1 =Label(window, text="Device Name",font=('arial',10,'bold'),bd=12,bg='gray',fg='white')
    label_DateTime_1 =Label(window, text="DateTime",font=('arial',10,'bold'),bd=12,bg='gray',fg='white')

    label_BusVal_1 =Label(window, text=bus,font=('arial',10,'bold'),bd=12,bg='cadet blue',fg='cornsilk')
    label_DeviceVal_1 =Label(window, text=device,font=('arial',10,'bold'),bd=12,bg='cadet blue',fg='cornsilk')
    label_DateTimeVal_1 =Label(window, text=datetime.date.today(),font=('arial',10,'bold'),bd=12,bg='cadet blue',fg='cornsilk')

    Triptitle_1.grid(columnspan=2,row=0)
    TripVac_1.grid(column=3,row=0)
    label_Bus_1.grid(column=0,row=1)
    label_Device_1.grid(column=2,row=1)
    label_DateTime_1.grid(column=4,row=1)

    label_BusVal_1.grid(column=1,row=1)
    label_DeviceVal_1.grid(column=3,row=1)
    label_DateTimeVal_1.grid(column=5,row=1)

    '''lblBook1 = Label(window,text = 'UnReserved')
    lblBook1.grid(row =3, column = 0)
    lblBook2 = Label(window,text = 'UnReserved')
    lblBook2.grid(row =3, column = 1)
    lblBook3 = Label(window,text = 'UnReserved')
    lblBook3.grid(row =4, column = 0)
    lblBook4 = Label(window,text = 'UnReserved')
    lblBook4.grid(row =4, column = 1)
    lblBook5 = Label(window,text = 'UnReserved')
    lblBook5.grid(row =5, columnspan = 2)'''

    '''for i in range (0,5):
        bookd = Button(window,text="Reserved", padx=5, pady=5)
        rc = divmod(i,4)
        r,c = rc[0], rc[1]
        bookd.grid(row=r+5, column=c)'''
    for i in range(len(trips)):
        #print(trips[i][1])
        txtAvail =trips[i][4]
        txtBook =trips[i][3]
        bookcounter=1
        if str(trips[i][1]) == str(Btn_txt):
            for j in range (0,int(txtAvail)):
                if int(bookcounter) <= int(trips[i][3]):
                    bookd = Button(window,text="RFID"+str(Btn_txt)+str(j), padx=5, pady=5,bd=1,bg='red',fg='powder blue')
                    rc = divmod(j,4)
                    r,c = rc[0], rc[1]
                    bookd.grid(row=r+7, column=c)
                    bookcounter +=1
                else:
                    bookd = Button(window,text="UnReserved", padx=5, pady=5,bd=1,bg='green',fg='powder blue')
                    rc = divmod(j,4)
                    r,c = rc[0], rc[1]
                    bookd.grid(row=r+7, column=c)
               
    #button.append(Button(root,text=txtTrip, padx=60, pady=30,command=lambda:button_click(device,txtTrip)))
    
    #frame_pass=Frame(window,height=50,width=900,relief=RAISED,bd=7,bg="gray")
    #frame_Pass.grid(column=0,row=2)   
    #lblTitle = Label(window,text = 'LIFT Info', font=('arial',50,'bold'),bg='powder blue',fg='black')
    #lblTitle.grid(row =0, column = 0, columnspan=2, pady=40)
#===============================================================================

#==================================Input data===================================
route = []
today = datetime.datetime.now()
with open('routes.csv','r') as f:
    routereader = csv.reader(f)
    route = list(routereader)
 
bus = route[0][0]
device = route[0][1]
busRName=route[0][2]
#==================================Test Print===================================
#print (today)
#print (bus)
#print (device)

#client.subscribe(device+"/trip_detail")
#time.sleep(30)

root = Tk()
root.geometry('660x360')

#Test Frame
#==================================Controls and data===================================
root.title("Welcome To LIFT System")
frame_name=Frame(root,height=50,width=900,relief=RAISED,bd=7,bg="gray")
frame_trip=Frame(root,height=150,width=900,relief=RAISED,bd=7,bg="powder blue")
#frame_pass=Frame(root,height=150,width=900,relief=RAISED,bd=7,bg="powder blue")

label_Bus =Label(frame_name, text="Bus Name",font=('arial',10,'bold'),bd=12,bg='gray',fg='white')
label_Device =Label(frame_name, text="Device Name",font=('arial',10,'bold'),bd=12,bg='gray',fg='white')
label_DateTime =Label(frame_name, text="DateTime",font=('arial',10,'bold'),bd=12,bg='gray',fg='white')

Triptitle=Label(frame_name, text=busRName,justify=CENTER,padx=250, pady=5,font=('arial',15,'bold'),bd=1,bg='powder blue',fg='green')
Tripinfo=Label(frame_trip, text="Trip Information",padx=10, pady=5,justify=CENTER,font=('arial',15,'bold'),bd=1,bg='powder blue',fg='green')

#entry_Bus =Entry(frame_name)
#entry_Device =Entry(frame_name)
#entry_DateTime =Entry(frame_name)
#entry_DateTime.text = today
#entry_Bus.text = bus
#entry_Device.text =device

label_BusVal =Label(frame_name, text=bus,font=('arial',10,'bold'),bd=12,bg='cadet blue',fg='cornsilk')
label_DeviceVal =Label(frame_name, text=device,font=('arial',10,'bold'),bd=12,bg='cadet blue',fg='cornsilk')
label_DateTimeVal =Label(frame_name, text=today,font=('arial',10,'bold'),bd=12,bg='cadet blue',fg='cornsilk')

Triptitle.grid(columnspan=7,row=0)
Tripinfo.grid(columnspan=5,row=0)

label_Bus.grid(column=0,row=1)
label_Device.grid(column=2,row=1)
label_DateTime.grid(column=4,row=1)

#entry_Bus.grid(column=1,row=1)
#entry_Device.grid(column=3,row=1)
#entry_DateTime.grid(column=5,row=1)

label_BusVal.grid(column=1,row=1,padx=10)
label_DeviceVal.grid(column=3,row=1)
label_DateTimeVal.grid(column=5,row=1)

#label_test =Label()
#label_test.grid(row=5,column=0)
#==================================read data===================================
trips = []
with open('trips.csv','r') as f:
    tripreader = csv.reader(f)
    trips = list(tripreader)


button = []
txtTrip = []
txtAvail = []
txtBook = []
btn_dict= {}
col=0

for i in range(len(trips)):
    txtTrip = trips[i][1]
    txtAvail =trips[i][4]
    txtBook =trips[i][3]
    #button.append(Button(root,text=txtTrip, padx=60, pady=30,command=lambda:button_click(device,txtTrip)))
    Trip_Button(txtTrip,i+4,device)
    #action = lambda:button_click(device,txtTrip)
    #btn_dict[i] =Button(frame_trip,text=trips[i][1], command=action)
    #rc = divmod(col,4)
    #r,c = rc[0], rc[1]
    #btn_dict[i].grid(row=r+1, column=c,padx=45, pady=10)
    #btn_dict[TripBut].grid(row=1,column=col,pady=5)
    #col +=1
    
#print (trips)
#print (txtAvail)
#print (txtBook)
 
    
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

