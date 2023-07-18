file = open("D:/bohubrihi/python programming/learn python/hello_world/file_io/test_file.txt","r")
print(file.read())

file.close()


#with statement diye file open korle auto file  close hoy 

with  open("D:/bohubrihi/python programming/learn python/hello_world/file_io/test_file.txt","r") as file:
      print(file.read())