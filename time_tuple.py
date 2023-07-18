import datetime

current_date_time = datetime.datetime.now()

struct_time_obj= current_date_time.timetuple()
print(struct_time_obj[0])
print(struct_time_obj[1])
print(struct_time_obj[2])