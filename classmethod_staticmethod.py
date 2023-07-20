class student:     #student class declare
    school_name ="test school"  #student class er statename school name
    def __init__(self, name, course):   #object declare
        self.name =name
        self.course= course
    @classmethod          #class method  declare
    def get_school_name(cls):
        return cls.school_name

student_one = student("s1","c1")  #object calling 
student_two = student("s2","c2")

print(student.get_school_name)  #class method call