# #zero division error control er jonno

def zero_division_error(func):
    def inner(a, b):
        if b == 0:
            return "zero division error"
        return func(a, b)  # Pass the arguments to the decorated function
    return inner

@zero_division_error
def divide(a, b):
    return a / b

print(divide(10, 2))  # Output: 5.0
print(divide(10, 0))  # Output: "zero division error"