from kafka import KafkaConsumer
import numpy as np
import json
# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'], value_deserializer=lambda m: json.loads(m.decode('utf-8')))

sensordata_temp = []
sensordata_co2 = []

if __name__ == "__main__":
    consumer.subscribe(topics=["sensordata", "rpc"])
    for message in consumer:
        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
        
        if message.topic == "sensordata":
            print("Received sensor data:" + str(message.value))
            sensordata_temp.append(int(message.value["temp"]))
            sensordata_co2.append(int(message.value["co2"]))
        elif message.topic == "rpc":
            if message.value == "sum":
                print("Sum Temp: %f" % (np.sum(sensordata_temp)))
                print("Sum CO2: %f" % (np.sum(sensordata_co2)))
            elif message.value == "avg" and len(sensordata_temp) > 0:
                print("Avg Temp: %f" % (np.average(sensordata_temp)))
                print("Avg CO2: %f" % (np.average(sensordata_co2)))
            elif message.value == "flush" and len(sensordata_temp) > 0:
                print("Flushing sensor data")
                sensordata_co2 = []
                sensordata_temp = []
            elif message.value == "min" and len(sensordata_temp) > 0:
                print("Min Temp: %f" % (np.min(sensordata_temp)))
                print("Min CO2: %f" % (np.min(sensordata_co2)))
            elif message.value == "max" and len(sensordata_temp) > 0:
                print("Max Temp: %f" % (np.max(sensordata_temp)))
                print("Max CO2: %f" % (np.max(sensordata_co2)))
            else:
                print("Unkown command or format")
        else:
            print("Unkown message format")
