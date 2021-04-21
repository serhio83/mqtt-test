# python mqtt testing scripts

## requirements

- python3
- paho-mqtt 1.5.1
- docker-ce

## run broker

```
docker run -d --name emqx -p 18083:18083 -p 1883:1883 emqx/emqx:latest
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
