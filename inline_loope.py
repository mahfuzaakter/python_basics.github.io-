my_list=[]

#normal loop
for i in range(1,101):
    my_list.append(i)

print(my_list)



#inline loop 
another_list =[i for i in range(1,100)]
print(another_list)

#example
numbers =[1,2,3,4,5,13,16,18,20]

even_numbers= [number for number in numbers if number %2 == 0]
print("even numbers",even_numbers)

odd_numbers= [number for number in numbers if number %2 != 0]
print("odd numbers",odd_numbers)