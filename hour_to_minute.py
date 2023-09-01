# def hours_to_minutes(hours):
#     # 1 hour is equal to 60 minutes
#     minutes = hours * 60
#     return minutes

# # Example usage:
# hours = float(input("enter hour:")) # Replace this with the number of hours you want to convert
# converted_minutes = hours_to_minutes(hours)
# print(f"{hours} hours is equal to {converted_minutes} minutes")

def hour_to_minute(hours):
        minutes = hours * 60
        return minutes
hours = float(input("enter hours:"))
convert= hour_to_minute(hours)
print(f"{hours} is equal to {convert} minutes")