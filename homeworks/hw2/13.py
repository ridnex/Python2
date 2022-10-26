import datetime
year = int(input())
month = int(input())
day = int(input())
x = datetime.datetime(year, month, day)
tomorrow = x + datetime.timedelta(days = 1)
print(tomorrow.strftime("%Y-%m-%d"))
