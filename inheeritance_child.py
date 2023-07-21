class person:             #person class create declare
    def __init__ (self, name, age, gender):     #object create
         self.name = name
         self.age = age
         self.gender = gender
         
    def introduce(self):         # method declare
     return "my name is {}".format(self.name)
    

class student( person):
       def __init__(self,name, age, course):
        
          self.course = course
          person.__init__(self, name, age,gender="") # type: ignore


student_one = student("user",26,["c","c++"])

print(student_one.introduce())  #introduce call by inherite          


