with  open("D:/bohubrihi/python programming/learn python/hello_world/file_io/test_file.txt","a") as file:
    my_list = ["this is item1\n","this is item2"]  
    file.write("this is for our program\n")
    file.writelines(my_list)