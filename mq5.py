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

def on_message(client, userdata, msg):
    print("On Messaged............")
    topic = msg.topic
    m_decode = str(msg.payload.decode("utf-8"))
    print("Message received: ", m_decode)

# b="test.mosquitto.org"
b="127.0.0.1"

client = mqtt.Client("LIFT2")

client.on_connect = on_connect
client.on_disconnect = on_disconnect
#client.on_log = on_log
client.on_message = on_message

print("Connecting to borker ",b)
client.connect(b)

client.loop_start()
client.subscribe("lift98/sensor1")
time.sleep(30)
client.loop_stop()

print("Disconnecting....")
client.disconnect()
