import paho.mqtt.client as mqtt
import time

broker = 'localhost'
port = 1883
topic = f'rpi/#'
client_id = 'sub1'
username = 'sub1'


def on_connect(client, userdata, flags, rc):
    print("mqtt: [{}:{}] {}".format(broker, port, mqtt.connack_string(rc)))
    client.subscribe(topic, qos=1)


def on_subscribe(client, userdata, mid, qos):
    print("mqtt: [{}] subscribed QoS: {}".format(topic, qos[0]))


def on_message(client, userdata, msg):
    print("mqtt: [{}] receive: {}".format(
        msg.topic,
        str(msg.payload.decode())))


if __name__ == "__main__":
    client = mqtt.Client(
        client_id, protocol=mqtt.MQTTv311, clean_session=False)
    client.on_connect = on_connect
    client.on_subscribe = on_subscribe
    client.on_message = on_message
    client.username_pw_set(username)
    client.connect(host=broker, port=port)
    client.loop_forever()
