from kafka import KafkaConsumer
from kafka import KafkaProducer
from kafka.errors import KafkaError
import numpy.random as np
import time
import json
import os
time.sleep(20)
print("FROST Import Service started!")

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(os.environ["subtopic"], bootstrap_servers=[os.environ["kafkainstance"] + ":" + os.environ["kafkaport"]], fetch_max_wait_ms=5000)
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("Just added the following to the FROST server: %s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
