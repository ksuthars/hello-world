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

def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected with result code " + str(rc))


b="127.0.0.1"
client = mqtt.Client("LIFT")

client.on_connect = on_connect
client.on_disconnect = on_disconnect
#client.on_log = on_log

print("Connecting to borker ",b)
client.connect(b)

client.loop_start()
client.publish("26051D64/trip_detail","[7488388939, 483993993, 3993993993, 27748488489]")
client.loop_stop()

print("Disconnecting....")
client.disconnect()
