import time
print(time.time())

seconds= 1689634479.5603878

print(time.ctime(seconds))

print(time.localtime(seconds))

print("i am new line")
time.sleep(2)
print("i am another line")


import datetime
print(datetime.datetime.now())

print(datetime.datetime.utcnow())

random_date=datetime.date.fromtimestamp(12345678)
print(random_date.year)
print(random_date.month)
print(random_date.day)