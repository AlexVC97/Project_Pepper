from publish import Publish
import paho.mqtt.client as mqtt

class ClientHandler():
    def __init__(self, broker_ip, broker_port):
        self.broker_ip = broker_ip
        self.broker_port = broker_port
        self.publish = Publish()
        self.client = mqtt.Client("PUB_CLIENT") # Create new instance

    def make_connection(self):
        mqtt.Client.connected_flag = False # Create flag in class
        self.client.on_log = self.publish.on_log
        self.client.on_connect = self.publish.on_connect
        self.client.on_disconnect = self.publish.on_disconnect
        self.client.on_publish = self.publish.on_publish
        self.client.connect(self.broker_ip, self.broker_port) # Establish connection
        self.client.loop_start()
        while not self.client.connected_flag: # Wait in loop
            print "In wait loop"
            time.sleep(1)
        time.sleep(3)

    def publishing(self, topic, msg):
        ret = self.client.publish(topic, msg, 0) # Publish
        print "Published return = " + str(ret)
        time.sleep(3)

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()
