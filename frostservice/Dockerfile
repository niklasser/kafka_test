FROM python:3

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY frostservice.py ./

ENV kafkainstance=kafka
ENV kafkaport=9092
ENV subtopic=sensordata
ENV resulttopic=mlresult

CMD [ "python", "-u", "./frostservice.py" ]
