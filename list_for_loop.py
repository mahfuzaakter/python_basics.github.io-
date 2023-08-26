aa=[4,5,6,7]
sum=0
# looping through list
for x in aa:
    sum=sum+ x
print(sum)
print(x)


fruits= ["banana","apple","orange"]

for y in fruits:
    
    
    if y == "apple":
        break
    print(y)  
    
#  nested loop 
adj=["red","big"]

for i in adj:
    for j in fruits:
        print(i,j)
        
print(fruits[1:])
fruits= ['banana','apple','orange']
fruits.append('mango')
print(fruits)
fruits.count('mango')
print(fruits)