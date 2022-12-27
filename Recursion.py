# # Recursion is the process of defining something in terms of itself.
# Factorial of number
def factorial(number):
    if (number == 1 or number ==0):
        return 1
    else:
        return number * factorial(number - 1)

print(factorial(5))


# Fibonacci Sequence
def fibonacci(number):
    if(number == 1):
        return 1
    elif(number == 0):
        return 0
    else:
        return fibonacci(number-1) + fibonacci(number-2)
print(fibonacci(6))