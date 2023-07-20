class person:             #person class create declare
    def __init__ (self, name, age, gender):     #object create
         self.name = name
         self.age = age
         self.gender = gender
         
    def introduce(self):         # method declare
     return "my name is {}".format(self.name)





person_one = person ( "user", 20,"female")    #object calling
print(person_one.introduce())          #method call