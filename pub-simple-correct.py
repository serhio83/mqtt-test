import paho.mqtt.client as mqtt
import time
import logging as logger

logger.basicConfig(filename='pub-simple-correct.log',
                   datefmt='%Y-%m-%d %H.%M.%S',
                   format='%(asctime)s.%(msecs)03d [%(name)s.%(threadName)s.%(funcName)s] %(message)s',
                   level=logger.DEBUG)
broker_url = "localhost"
broker_port = 1883


def on_connect(client, userdata, flags, rc):
    # print("mqtt: on_connect {}".format(mqtt.connack_string(rc)))
    client.publish("rpi/pub-simple", "correct payload 1", 1)


client = mqtt.Client()
client.on_connect = on_connect
client.enable_logger(logger)
client.connect(broker_url, broker_port)

client.message_retry_set(0.1)
client.loop_start()
time.sleep(0.5)
client.loop_stop()
