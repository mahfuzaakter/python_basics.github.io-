countries = ["bangladesh","india","usa","uk"]


print(countries)
print(countries[0])   #only 0 index item print

countries[0]="germany"    #for change item
print(countries)

del countries[1]       #delete item
print(countries)

countries.pop()

print(countries)

numbers = [1,2,3,4,5,6]
print(numbers[:])