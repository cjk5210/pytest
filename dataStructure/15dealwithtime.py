import time
def calcProd():
    product=1
    for i in range(1,100000):
        product=product*i
    return product

def calcTime():
    startTime=time.time()
    prod=calcProd()
    endTime=time.time()
    print('The result is %s digits long.'% (len(str(prod))))
    print('Took %s seconds to calculate.' % (endTime-startTime))
#calcTime()

def testTimeSleep():
    for i in range(20):
        print('Tick')
        time.sleep(1)
        print('Tock')
        time.sleep(1)
#testTimeSleep()

def roundNumber():
    now=time.time()
    print(now)
    print(round(now,2))
    print(round(now,4))
    print(round(now))
    print(type(now))
#roundNumber()

import datetime

def getSysTime():
    dt=datetime.datetime.now()
    print(dt)
    dt=datetime.datetime(1987,7,2,16,40,26)
    print(dt.year,dt.month,dt.day)
    print(dt.hour,dt.minute,dt.second,dt.microsecond)
#getSysTime()
def convertUnixTimeToDateTime():
    dt=datetime.datetime.fromtimestamp(1000000)
    print(dt)
    dt=datetime.datetime.utcfromtimestamp(time.time())
    print(dt)
#convertUnixTimeToDateTime()

def compareWithDateTime():
    halloween2015=datetime.datetime(2015,10,31,0,0,0)
    newyears2016=datetime.datetime(2016,1,1,0,0,0)
    oct31_2015=datetime.datetime(2015,10,31,0,0,0)
    print(halloween2015==oct31_2015)
    print(halloween2015>newyears2016)
    print(newyears2016>halloween2015)
    print(newyears2016!=halloween2015)
#compareWithDateTime()

def testTimePeriod():
    delta=datetime.timedelta(days=11,hours=10,minutes=9,seconds=8)
    print(delta.days,delta.seconds,delta.microseconds)
    print(delta.total_seconds())
#testTimePeriod()

def testTimeBeforeAPeriod():
    dt=datetime.datetime.now()
    print(dt)
    thousandDays=datetime.timedelta(days=1000)
    print(dt+thousandDays)
#2017-11-21 14:03:18.452422
#2020-08-17 14:03:18.452422
#testTimeBeforeAPeriod()

def timeToStr():
    oct21st=datetime.datetime(2015,10,21,16,29,0)
    print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
    print(oct21st.strftime('%I:%M %p'))
    print(oct21st.strftime("%B of '%y"))
#timeToStr()

def strToTime():
    print(datetime.datetime.strptime('October 21, 2015','%B %d, %Y'))
    print(datetime.datetime.strptime('2015/10/21 16:29:00','%Y/%m/%d %H:%M:%S'))
strToTime()