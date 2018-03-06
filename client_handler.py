from publish import Publish
import paho.mqtt.client as mqtt

class ClientHandler():
    def __init__(self, broker_ip, broker_port):
        self.broker_ip = broker_ip
        self.broker_port = broker_port

    def make_connection(self):
        publish = Publish()
        mqtt.Client.connected_flag = False # Create flag in class
        client = mqtt.Client("PUB_CLIENT") # Create new instance
        client.on_log = publish.on_log
        client.on_connect = publish.on_connect
        client.on_disconnect = publish.on_disconnect
        client.on_publish = publish.on_publish
        client.connect(self.broker_ip, self.broker_port) # Establish connection
        client.loop_start()
        while not client.connected_flag: # Wait in loop
            print "In wait loop"
            time.sleep(1)
        time.sleep(3)

    def publish(self, topic, msg):
        ret = client.publish(topic, msg, 0) # Publish
        print "Published return = " + str(ret)
        time.sleep(3)

    def disconnect(self):
        client.loop_stop()
        client.disconnect()
