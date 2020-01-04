# na poczatku tylko z pliku testowego potem przepięcie na API

from kafka import KafkaProducer
from time import sleep
from json import dumps

# producer = KafkaProducer(bootstrap_servers=[''], value_serializer=lambda x: dumps(x).encode('UTF-8'))

for e in range(1, 10):
    data = {'value': e}
    # producer.send('test_topic', value=data)
    sleep(5)
