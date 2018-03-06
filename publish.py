import paho.mqtt.client as mqtt
import time
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
file_handler = logging.FileHandler("logging.pepper.out")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class Publish():
    def on_log(self, client, userdata, level, buf):
        logger.info(buf)

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            client.connected_flag = True # Set flag
            logger.info("connected OK")
        else:
            logger.info("bad connection returned code = " + str(rc))
            client.loop_stop()

    def on_disconnect(self, client, userdata, rc):
        logger.info("client disconnected OK")

    def on_publish(self, client, userdata, mid):
        logger.info("in on_pub callback mid = " + str(mid))
