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
def  a(fname, **lname):
   fname= "ila"+ lname
   return 

print(a(1,2.100,25,75))