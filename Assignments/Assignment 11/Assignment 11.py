import Clock
import time
seconds = 0
hours = int(input("What is the current hour ==> "))
minutes = int(input("What is the current minute ==> "))
seconds = int(input("What is the current second ==> "))
myClock = Clock(hours, minutes, seconds)
while True:
    print(myClock)
    myClock.tick()
    time.sleep(1)