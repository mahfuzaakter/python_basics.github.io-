def my_function(fname):  #Parameters  function define
  print("Good morning! " + fname)

my_function("Emil")  #Arguments   function call
my_function("Tobias")
my_function("Linus")


def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#You can also send arguments with the key = value syntax.
#This way the order of the arguments does not matter.

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# default parameter value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# return statement
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


# docstring
def Add(a, b):
    '''
    This will take two parameter
    Return value is integer
    '''
    return a + b


print(Add(10, 20))
print(Add.__doc__)

# lambda function
def cube(y):
  return y * y * y

print(cube(5))

lambda_cube = lambda y: y * y * y

# using the lambda function
print(lambda_cube(6))


# map function
def myfunc(a):
  return len(a)

x = map(myfunc, ('apple', 'banana', 'cherry'))
print(list(x))


def square(x):
    return x*x

num = [1, 2, 3, 4, 5]
result = list(map(square, num))

print(result)


# filter function
ages = [5, 12, 17, 18, 24, 32]
def myFunc(x):
  if x < 18:
    return False
  else:
    return True

# adults = list(filter(myFunc, ages))
adults = tuple(filter(myFunc, ages))
print(adults)


num = [5, 12, 17, 18, 25, 32]

result = list(filter(lambda x: x%2==0, num))

print(result)
print(num)



# Generator
def ten(a,b):
    if a>b:
       a==1+2
    yield 11
 
val= ten(12,13)
print(val.__next__())
print(val)


# Recursion
# factorial
def fact(n):
   if n==0:
      return 1
   else:
      return n,fact (n-1)
   
print(fact(10))


# arg and **kwarg
