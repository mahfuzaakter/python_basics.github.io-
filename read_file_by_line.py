
file = open("D:/bohubrihi/python programming/learn python/hello_world/file_io/test_file.txt", "r")
print(file.readline())


#loop er maddhome
while True:
    line = file.readline()
    if not line:
        break
    print(line)

all_lines = file.readline()
print(all_lines)