import paho.mqtt.client as mqtt
import time

broker_url = "localhost"
broker_port = 1883


def pub(client, list):
    for x in list:
        time.sleep(0.1)
        result = client.publish("rpi/pub-simple", x, 1)
        status = result[0]
        if status == 0:
            print(f"mqtt: publish {x}")
        else:
            print(f"Failed to publish message")
    client.loop_write()


if __name__ == '__main__':
    list = ['payload1', 'payload2', 'payload3']
    client = mqtt.Client()
    client.connect(broker_url, broker_port)
    client.loop_start()
    pub(client, list)
