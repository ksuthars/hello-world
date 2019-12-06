import serial, time
ser = serial.Serial("/dev/ttyS0")
ser.baudrate = 9600
ser.timeout = 0

string=""

while True:
    string = ser.read(12)

    if len(string) == 0:
        print("Please wave a tag")

    else:
        string = string[1:11]   # Strip header/trailer
        print("string",string)
        if string == 'E0043DBB52':
            print("hello Joe, what do you know?")
    print(string)
