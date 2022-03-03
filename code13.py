#Fibonacci number in a given range

# def fibonacci(n):
#     if n < 0:
#         print("Incorrect input")

#     elif n == 0 :
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# n = int(input("Enter the number: "))
# print(fibonacci(n))


def fib(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect Input")
    elif n == 1:
        print(a)
    else:
        print(a)
        print(b)

        for i in range(2,n):
            c = a+b
            a = b 
            b = c
            print(c)
fib(8)


    