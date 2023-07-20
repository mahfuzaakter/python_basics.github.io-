# class person:

   
#     name = "mahfuza"
# object1 =person()
# print(object1)
# print(type(object1))



class person:
    def __init__ (self, name, age, gender):
         self.name = name
         self.age = age
         self.gender = gender

person_one = person ( "user", 20,"female")
print(person_one.name)
print(person_one.age)
print(person_one.gender)