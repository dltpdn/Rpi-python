import time, datetime

print time.time()
print time.localtime()
print time.strftime('%Y-%m-%d %H:%M:%S')

today = datetime.date.today()
print today.year, today.month, today.day, today.weekday()

today = datetime.datetime.today()
print today.year, today.month, today.hour, today.minute