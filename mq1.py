#!python3
import paho.mqtt.client as mqtt
import time

b="test.mosquitto.org"
client = mqtt.Client("LIFT")
print("Connecting to borker ",b)
client.connect(b)
time.sleep(4)
print("Disconnecting....")
client.disconnect()
