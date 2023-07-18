from datetime import datetime
current_datetime = datetime.now()
print(current_datetime)


#strftime()

print(datetime.strftime(current_datetime,"%d%n%y %H:%M:%S"))