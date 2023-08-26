def grade(score):
    if score>=90 and score<=100:
             return "A"
    elif score >=80:
             return "B"
    elif score>=70:
             return "C"
    elif score>=60:
             return "D"
    elif score>=50:
             return "E"
    elif score>=40:
            return "E-"
    elif score<40:
           return "F" 
score=int(input("enter the student score:"))
grade=grade(score)
print(f"the studen grade is: {grade}")