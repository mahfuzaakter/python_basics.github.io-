fruits={"mango","apple","orange" ,1,2,1.5}
print(fruits)
print(type(fruits))

fruits = set(["a","b"])
print(fruits)
print(type(fruits))

print("mango" in fruits)

#add  set item
user={"surah", "hossain"}
user.add("hasan")
user.add((1,2,3))

print(user)

#remove set item

user.remove("hasan")
print(user)

user.discard((1,2,3))
print(user)