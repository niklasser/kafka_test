from kafka import KafkaConsumer
from kafka import KafkaProducer
from kafka.errors import KafkaError
import numpy.random as np
import time
import json
import os
print("ML Service started!")
print("sleeping....")
time.sleep(20) 

producer = KafkaProducer(bootstrap_servers=[os.environ["kafkainstance"] + ":" + os.environ["kafkaport"]], value_serializer=lambda v: json.dumps(v).encode('utf-8'))
print("Producer init")
# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(os.environ["subtopic"], bootstrap_servers=[os.environ["kafkainstance"] + ":" + os.environ["kafkaport"]])

print("Consumer init")               
for message in consumer:
    print("Received new sensor value, will infer now..")
    msg = {"result":str(np.randint(0, 1))}
    producer.send(os.environ["resulttopic"], msg)
    print("Sending result to Kafka..✅")

