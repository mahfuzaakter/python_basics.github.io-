def my_func():
    for i in range(1,11):
       print(i)

my_func()


# recursion
def my_function(n):
    if n>10:
        return
    print(n)
    my_function(n+1)

my_function(1)    
