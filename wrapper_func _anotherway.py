def my_func():
    print("hello world")

def print_function(func):
    func()
    print("this is from print function")


    
def greet(func):
  def inner():
       func()
       print("this is inner function")
  return inner       

@greet
def hello():
    print("this is hello function")

print(hello())
  