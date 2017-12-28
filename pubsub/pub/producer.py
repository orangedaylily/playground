#!/usr/bin/env python
import logging, time
import multiprocessing

from kafka import KafkaProducer
from constants import CONST


class Producer(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)
        self.stop_event = multiprocessing.Event()

    def stop(self):
        self.stop_event.set()

    def run(self):
        producer = KafkaProducer(bootstrap_servers=CONST.BOOTSTRAP_SERVER)

        while not self.stop_event.is_set():
            producer.send(CONST.TOPIC1, b"test")
            #producer.send(CONST.TOPIC2(), b"\xc2Hola, mundo!")
            time.sleep(1)

        producer.close()

def main():
    tasks = [
        Producer(),
    ]

    for t in tasks:
        t.start()

    #time.sleep(10)

    #for task in tasks:
        #task.stop()

    #for task in tasks:
        #task.join()


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.DEBUG
    )
    main()
