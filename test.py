score = int(input("Enter the student's score: "))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
elif 60 <= score < 70:
    grade = "D"
elif 50 <= score < 60:
    grade = "E"
elif 40 <= score < 50:
    grade = "E-"
else:
    grade = "F"

print(f"The student's grade is: {grade}")

def user_name(first,last):
    print("name is: {}".format(first))




