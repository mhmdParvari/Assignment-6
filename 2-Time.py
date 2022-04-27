class Time:
    def __init__(self,_hour,minute,second):
        self.hour=_hour
        self.min=minute
        self.sec=second

    def fix_time(self):
        if self.sec>=60: 
            self.sec-=60
            self.min+=1
        if self.min>=60:
            self.min-=60 
            self.hour+=1
        return self

    def __add__(self,time2):
        return Time(self.hour+time2.hour,self.min+time2.min,self.sec+time2.sec).fix_time()

    def sec_to_time(self,seconds):
        self.hour=int(seconds/3600)
        t=seconds%3600
        self.min=int(t/60)
        self.sec=t%60

    def time_to_sec(self):
        return self.hour*3600+self.min*60+self.sec

    def show(self):
        print(self.hour,end='')
        print(':',end='')
        print(self.min,end='')
        print(':',end='')
        print(self.sec)

a=Time(2,5,10)
b=Time(1,3,55)
c=a+b
c.show()
print(c.time_to_sec())

