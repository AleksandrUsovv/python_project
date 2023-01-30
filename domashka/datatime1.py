import datetime
# # 1 part. Что то я не осилил и не заработал у меня код. не смог найти ошибку...
# sample1 = 'Jan 1 2014 2:43PM'
# sample2 = '14:20 10/12/22'  # YY/MM/DD
# sample3 = 'Tuesday, September 24, 2019'
# sample4 = '01.01.1970 - 00:00:01'
#
# new_date1 = datetime.datetime.strptime(sample1, '%b %d %Y %-I:%M%p')
# print(new_date1)
# new_date2 = datetime.datetime.strptime(sample2, '%H:%M %-y/%m/%d')
# print(new_date2)
# new_date3 = datetime.datetime.strptime(sample3, '%A, %B %d, %Y')
# print(new_date3)
# new_date4 = datetime.datetime.strptime(sample4, '%d.%m.%Y - %H:%M:%f')
# print(new_date4)

# # 2 part
# today = datetime.date.today()
# tdelta = datetime.timedelta(days = 1)
# yesterday = today - tdelta
# tomorrow = today + tdelta
# print('Yesterday : ',yesterday)
# print('Today : ',today)
# print('Tomorrow : ',tomorrow)

# # 3 part
# some_day = 1014163200
# print(datetime.datetime.utcfromtimestamp(some_day).strftime("%d.%m.%Y"))

# # 4 part
# week_delta = datetime.timedelta(days=14)
# timestamp = datetime.datetime.now().timestamp()
# ourdate = datetime.datetime.fromtimestamp(timestamp)
# def weeks_substruction():
#     return ourdate - week_delta
#
# print(timestamp)
# print(datetime.datetime.timestamp(weeks_substruction()))