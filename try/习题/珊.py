'''
# 第二题
class Time():
    def __init__(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second

# 第三题
class Date():
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

# 第四题
class Datetime(Date,Time):
    pass
'''

'''
# 第五题
class Time():
    def __str__(self):
        pass

class Date():
    def __str__(self):
        pass

class Datetime(Date,Time):
    pass

print(Time,Date,Datetime)
'''

# 第六题
class Time():
    def __str__(self):
        pass

class Date():
    def __str__(self):
        pass

class Datetime(Date,Time):
    def Date(self):
        pass
    def Time(self):
        pass
