# python mqtt testing scripts

## requirements

- python3
- paho-mqtt 1.5.1
- docker-ce

## run broker

```
docker run -e "DOCKER_VERNEMQ_ALLOW_ANONYMOUS=on" \
           -e "DOCKER_VERNEMQ_ACCEPT_EULA=yes" \
           -e "DOCKER_VERNEMQ_PERSISTENT_CLIENT_EXPIRATION=1m" \
           -e "DOCKER_VERNEMQ_MAX_ONLINE_MESSAGES=-1" \
           -e "DOCKER_VERNEMQ_MAX_OFFLINE_MESSAGES=-1" \
           -e "DOCKER_VERNEMQ_ALLOW_MULTIPLE_SESSIONS=off" \
           --name vernemq1 --rm -d -p 1883:1883 -p 8888:8888 vernemq/vernemq

```

## usage

- `sub.py` starts client, subscribe on topic & listen message queue
- `pub.py` startrs publisher for sending messages
- `pub-simple-wrong.py` example script with duplicating messages
- `pub-simple-correct.py` fixed example script

## testing

- run `sub.py`
- run `pub-simple-wrong.py` & wait on subscriber side, after publishing repeat again
- see other examples `pub.py` / `pub-simple-correct.py` / `publish-generator.py`
