import paho.mqtt.client as mqtt
import time
import logging

class Communication():
    def on_log(self, client, userdata, level, buf):
        logging.info(buf)

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            client.connected_flag = True # Set flag
            logging.info("connected OK")
        else:
            logging.info("bad connection returned code = " + str(rc))
            client.loop_stop()

    def on_disconnect(self, client, userdata, rc):
        logging.info("client disconnected OK")

    def on_publish(self, client, userdata, mid):
        logging.info("in on_pub callback mid = " + str(mid))
