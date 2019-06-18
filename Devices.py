import datetime

class SimpleDevice(object):

    def __init__(self, string, delay):
        self.string = string
        self.delay = delay
        self.start_time = datetime.datetime.now()
        self.datetime_format = "%Y-%m-%d %H:%M%S.%f"
        self.start_time = self.start_time.replace(microsecond=0)
        # self.start_time = self.start_time.replace(second=0)

    def run(self):
        current_time = datetime.datetime.now()
        diff = current_time - self.start_time
        if diff.seconds % self.delay == 0:
            print(self.string)
        