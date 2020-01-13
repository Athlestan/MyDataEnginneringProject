from kafka import KafkaProducer
from time import sleep
from json import dumps
from datetime import datetime

producer = KafkaProducer(bootstrap_servers=['quickstart.cloudera:9092'], value_serializer=lambda x: dumps(x).encode('UTF-8'))

for e in range(1,10):
    data = {'id': datetime.now().strftime("%Y-%m-%d:%H:%M:%S"), 'value': e}
    producer.send('extract_data', value=data)
    sleep(5)
