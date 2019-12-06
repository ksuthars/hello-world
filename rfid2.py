import time
import serial
          
      
data = serial.Serial("/dev/ttyS0")
data.baudrate = 9600
data.timeout=1
print(" ")
          
try:     
    while 1:
         #x=data.readline()#print the whole data at once
         #x=data.read()#print single data at once
         
        print("Place the card")
        x=data.read(12) #print upto 10 data at once and the 
#        time.sleep(1)
        print(x)
         
        if x=="0002862532":
            print("Card No - ",x)
            print("Welcome Bala")
            print(" ")
         
        elif x=="0002863625":
            print("Card No - ",x)
            print("Welcome Teja")
            print(" ")
      
            

        else:
            print("Wrong Card.....")
            print(" ")        
         
        print(x)

except KeyboardInterrupt:
        data.close()
