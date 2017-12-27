#!/usr/bin/env python
import logging, time
import multiprocessing

from kafka import KafkaConsumer
from constants import CONST

class Consumer(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)
        self.stop_event = multiprocessing.Event()

    def stop(self):
        self.stop_event.set()

    def run(self):
        consumer = KafkaConsumer(bootstrap_servers=CONST.BOOTSTRAP_SERVER,
                                 auto_offset_reset='earliest',
                                 consumer_timeout_ms=1000)
        consumer.subscribe([CONST.TOPIC1])

        while not self.stop_event.is_set():
            for message in consumer:
                print(message)
                if self.stop_event.is_set():
                    break

        consumer.close()


def main():
    tasks = [
        Consumer()
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
        level=logging.INFO
    )
    main()
