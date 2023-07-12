num = [9,2,7,4,6,8,3,5,1]

num.sort()
print(num)

another_num = [9,2,7,4,6,8,3,5,1]
sorted_num= sorted(another_num)
print(sorted_num)


#copy list using .copy() method
numb = [9,2,7,4,6,8,3,5,1]

another_num= numb.copy()
print(another_num)


copy_num =list(numb)
print(copy_num)


slice_num= numb[5::1]
print(slice_num)


#join list

merged_list = num + numb
print(merged_list)