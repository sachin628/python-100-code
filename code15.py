# Factorial of a number

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
num = 5
ans = factorial(num)
print("The factorial of", num, "is", ans)
