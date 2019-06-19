import datetime

class SimpleDevice(object):

    def __init__(self, string, delay):
        self.string = string
        self.delay = delay
        self.start_time = datetime.datetime.now()
        self.datetime_format = "%Y-%m-%d %H:%M%S.%f"
        self.start_time = self.start_time.replace(microsecond=0)
        self.printed = False
        self.start = True
        # self.start_time = self.start_time.replace(second=0)

    def run(self):
        current_time = datetime.datetime.now()
        diff = current_time - self.start_time

        if current_time.second == self.start_time.second:
            self.start = False
            return

        if diff.seconds % self.delay == 0 and not self.printed and not self.start:
            print(self.string)
            print("It's been {0} seconds since the last print. The elapsed time is {1} second(s).".format(self.delay, diff.seconds))
            self.printed = True
        elif diff.seconds % self.delay != 0 and self.printed:
            self.printed = False