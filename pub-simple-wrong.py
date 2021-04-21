import paho.mqtt.client as mqtt
import time
import logging as logger

logger.basicConfig(filename='pub-simple-correct.log', datefmt='%Y-%m-%d %H:%M:%S %z',
                   format='%(asctime)s [%(name)s.%(threadName)s.%(funcName)s] %(message)s', level=logger.DEBUG)
broker_url = "localhost"
broker_port = 1883
client = mqtt.Client()
client.enable_logger(logger)
client.connect(broker_url, broker_port)

# эта ручка задаёт интервал
client.message_retry_set(0.1)
client.loop_start()
client.publish("rpi/pub-simple", "wrong payload 1", 1)
client.loop_stop()
