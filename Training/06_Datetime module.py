#from datetime import date

# mydate = date(2022,5,12)
# print(mydate)
#
# mydate1 = date(2022,12,40)       #valueerror as day is out of range
# print(mydate1)

# mydate2 = date(2021,3,'21')        #typeerror as only integers can be passed
# print(mydate2)
#
# Today = date.today()
# print(Today.day)
# print(Today.month)
# print(Today.year)

# from datetime import datetime
# date_time = datetime.fromtimestamp(1887639468)
# print(date_time)

#convert date to string
# from datetime import date
# today = date.today()
# date = date.fromtimestamp(1887639468)
# print(date)
#
# String = today.isoformat()
# print(String)
# print(type(String))
#
# print(today.weekday())              #0 - monday , 6-sunday

# from datetime import time
# mytime = time(12,45,34)
# print(mytime)
# print(mytime.hour)
# print(mytime.minute)
# print(mytime.second)
# print(mytime.microsecond)
#
# #converting time object to string
# print(type(mytime))
# string = mytime.isoformat()
# print(string)
# print(type(string))
#

# mytime = time(hour=14)                #time with one argument
# print(mytime)
#
# mytime = time()                       #time with no argument
# print(mytime)
#
# from datetime import datetime
# date = datetime(2022,3,23)
# print(date)
#
# datetime = datetime(2021,4,2,23,12,54,2345)
# print(datetime)
# print(datetime.date())
# print(datetime.time())
# print(datetime.hour)
# print(datetime.timestamp())
# print(datetime.timetz())
# print(datetime.today())
# print(datetime.now())

#getting current date and time
# import datetime
# current_datetime = datetime.datetime.now()
# print(current_datetime)
#
# #getting current date
# current_date = datetime.date.today()
# print(current_date)
# print(dir(datetime))         #prints list containing all attributes

#difference between two dates and time
# from datetime import datetime,date
# date1 = date(2012,4,25)
# date2 = date(2022,3,21)
# difference = date2-date1
# print(difference)
# print(type(difference))
#
# time1= datetime(2022,4,4,6,5,34)
# time2= datetime(2022,4,2,4,6,32)
# diff = time1-time2
# print(diff)
# print(type(diff))

from datetime import timedelta
# list = dir(timedelta)
# for i in list:
#     if '_' not in i:
#         print(i,end=' ')
#
# t1 = timedelta(weeks=4,days=23,hours=21,minutes=34,seconds=24)
# t2 = timedelta(weeks=2,days=12,hours=13,minutes=23,seconds=12)
# dif = t1-t2
# print(dif)
# print(t1.total_seconds())

#formatting date with strftime, datetime to string
# from datetime import datetime
# today = datetime.now()
# print(today)
# print(today.strftime("%H:%M:%S"))
# print(today.strftime("%d:%B:%Y"))#%Y - year [0001,..., 2018, 2019,..., 9999]
                            # %m - month [01, 02, ..., 11, 12]
                            # %d - day [01, 02, ..., 30, 31]
                            # %H - hour [00, 01, ..., 22, 23
                            # %M - minute [00, 01, ..., 58, 59]
                            # %S - second [00, 01, ..., 58, 59]
                            #%B - month name

# #string to datetime object with strptime
# from datetime import datetime
# date_string = '12-11-1992'
# date_object = datetime.strptime(date_string,'%d-%m-%Y') # according to string formation needs to be done
# print(date_object)

#handling timezone
from datetime import datetime
import pytz
timezone_london = pytz.timezone('Europe/London')
datetime_l = datetime.now(timezone_london)
print(datetime_l.strftime('%d- %m- %Y'))


