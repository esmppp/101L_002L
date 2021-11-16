class Clock():
    def __init__(self, hour, min, sec, type =0):
        self.hour = hour
        self.minute = min
        self.sec = sec
        self.type = type
    
    def __str__(self):
        if self.type == 1:
            if(self.hour > 12):
                time = 'pm'
            else:
                time = 'am'
            return"{:2}:{:2}:{:0>2} {}".format(self.hour, self.minute,self.sec, time)
        else:
            return"{:2}:{:2}:{:0>2}".format(self.hour, self.minute,self.sec)

    def tick(self):
        self.sec += 1
        if self.sec == 60:
            self.minute += 1
            self.sec = 0
        if self.minute == 60:
            self.hour += 1
            self.minute = 0
        if self.type == 1:
            if self.hour == 13:
                self.hour = 1
                
if __name__ == '__main__':
    import time
    seconds = 0
    hours = int(input("What is the current hour ==> "))
    minutes = int(input("What is the current minute ==> "))
    seconds = int(input("What is the current second ==> "))
    myClock = Clock(hours, minutes, seconds, 1)
    while True:
        print(myClock)
        myClock.tick()
        time.sleep(1)