# 1.Write a program to make another list of duplicate elements from the following list
# [1, 5, 6, 5, 1, 2, 3]

list= [1, 5, 6, 5, 1, 2, 3]

lst=[]
for i in list:
    if list.count(i)>1 and i not in lst:
        lst.append(i)
    list.extend(lst)

print(list)
print(lst)
# print(list)

# print(list.count(i))
