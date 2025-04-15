import datetime
#Task 1.
print("Task 1.")

x = datetime.datetime.now()
solve = x - datetime.timedelta(days = 5)
print(solve)

#Task 2.
print("Task 2.")

current_time = datetime.datetime.now()
yesterday = current_time - datetime.timedelta(days = 1)
tomorrow = current_time + datetime.timedelta(days = 1)
print(yesterday.strftime("%x"), current_time.strftime("%x"), tomorrow.strftime("%x"))

#Task 3.
print("Task 3.")

time = datetime.datetime.now()
time2 = time.replace(microsecond = 0)
print(time2)

#Task 4.
print("Task 4.")

date1 = datetime.datetime(2021, 2, 12, 14, 30, 5)
date2 = datetime.datetime(2021, 2, 15, 16, 22, 3)

difference = date2 - date1
dif_secs = difference.total_seconds()
print(dif_secs)