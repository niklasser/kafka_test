from kafka import KafkaProducer
from kafka.errors import KafkaError
import numpy.random as np
import time
import json
producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda v: json.dumps(v).encode('utf-8'))

commands = ["sum", "avg", "flush", "min", "max"]

def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)


def sensor_or_rpc():
    return np.randint(100) < 80

if __name__ == "__main__":
    #Sending random sensor data
    while True:
        if sensor_or_rpc():
            msg = {"temp":str(np.randint(-20, 42)), "time":str(time.time_ns()), "co2":str(np.randint(1,1000))}
            producer.send("sensordata", msg)
            print("Send sensor data: " + str(msg))
        else:
            msg = np.choice(commands)
            producer.send("rpc", msg)
            print("Sending rpc: " + str(msg))
        time.sleep(np.randint(1, 10))
