FROM python:3

ADD  constants.py /
ADD  producer.py /

RUN pip install kafka-python

CMD [ "python", "./producer.py"]
