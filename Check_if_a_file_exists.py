path = "D:/bohubrihi/python programming/learn python/hello_world/file_io/test_file.txt"

#os.path
import os
print(os.path.isfile(path))

#pathlib
import pathlib
file = pathlib.Path(path)
print(file. is_file())