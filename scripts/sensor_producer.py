from kafka import KafkaProducer
from kafka.errors import KafkaError
import numpy.random as np
import time
import json
producer = KafkaProducer(bootstrap_servers=['localhost:19092'], value_serializer=lambda v: json.dumps(v).encode('utf-8'))

#Sending random sensor data
while True:
    msg = {"temp":str(np.randint(-20, 42)), "time":str(time.time_ns()), "co2":str(np.randint(1,1000))}
    producer.send("sensordata", msg)
    print("Send sensor data: " + str(msg))
    time.sleep(np.randint(1, 10))

def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)

