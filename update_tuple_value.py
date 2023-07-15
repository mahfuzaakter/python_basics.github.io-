fruits=("mango","apple","orange" ,1,2,1.5,["a","b"])
fruits=list(fruits)
print(fruits)
fruits[1]="grape"
print(type(fruits))
fruits=tuple(fruits)
print(fruits)
print(type(fruits))
