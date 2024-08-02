import random
from detection_method import detection_method

class test_detection(detection_method):
    def __init__(self, data):
        self.weight = data['weight']
        self.url = data['url']

    def start(self):
        pass

    def compute(self, values, index):
        values[index] = random.random()

    def shutdown(self):
        print("Shutting down...")