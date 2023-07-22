# 5!= 5*4*3*2*1=120
def factorial(n):
    if n==1:
        return 1
    m = factorial(n-1)
    return n*m


factorial(5)