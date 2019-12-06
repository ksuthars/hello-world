#!python3
import paho.mqtt.client as mqtt
import time

def on_log(client, userdata, level, buf):
    print("log: "+buf)

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Connected OK")
    else:
        print("Bad connection, returned code is ", rc)


b="test.mosquitto.org"
client = mqtt.Client("LIFT")

client.on_connect = on_connect
client.on_log = on_log

print("Connecting to borker ",b)
client.connect(b)

client.loop_start()
time.sleep(4)
client.loop_stop()

print("Disconnecting....")
client.disconnect()
