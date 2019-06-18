from Devices import SimpleDevice
import time, datetime

if __name__ == "__main__":
    tick1 = SimpleDevice("Hello World", 5)
    tick2 = SimpleDevice("Hello Buddy", 10)


    while True:

        tick1.run()
        tick2.run()
        # time.sleep(.1)