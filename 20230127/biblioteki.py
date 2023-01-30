import calendar

# print(calendar.month(1993, 12, w=10, l=2))
# print(calendar.calendar(2020, c=10))
# print(calendar.weekday(2023, 1, 27))
# print(calendar.isleap(2023))
# print(calendar.leapdays(2000, 2020))
# print(calendar.HTMLCalendar().formatmonth(2023, 1))

import time

#start = time.time()
# time.sleep(5)
# print(time.asctime())
# print(time.gmtime())
# print(time.localtime())
#
# # stop = time.time()
# # print(stop - start)

import datetime
d = datetime.date(2021, 1, 27)

print(d)
#
today = datetime.date.today()
print(today - d)

tdelta = datetime.timedelta(days=365, minutes=12, hours=12)
print(tdelta.total_seconds())

print(today.weekday())
print(today.isoweekday())

t = datetime.time(14, 25, 10, 456)
tdelta = datetime.timedelta(minutes=5)
print(tdelta)
print(type(t))

dt = datetime.datetime(2020, 11, 3, 12, 23, 12)
tdelta = datetime.timedelta(days=7, hours=15, minutes=33)
print(dt - tdelta)
print(dt.date())
print(dt.time())

today = datetime.datetime.now() #ili datetime.datetime.today()
print(today)

print(today.strftime('%A-%d.%m.%Y'))

dt_str = 'November 30, 2020 15:23'

new_date = datetime.datetime.strptime(dt_str, '%B %d, %Y %H:%M')
print(new_date)

print(today.timestamp())
print(datetime.datetime.fromtimestamp(1674845587.303005))