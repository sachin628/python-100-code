#Reverse of a number
'''
n= (input("Enter the digit:"))
n =(n[::-1])
print(n)
'''

# num =int( input("Enter the number which you want to reverse:"))
# reversed_num = 0
# while num != 0:
#     digit = num % 10
#     reversed_num = reversed_num * 10 + digit
#     num //= 10

# print("Reversed Number: " + str(reversed_num))


def getSum(n):
    reversed_num = 0
    while n != 0:  
        digit = n % 10
        reversed_num = reversed_num *10 + digit
        n //= 10

    
    return reversed_num
n = int(input("Enter the number:"))
print(getSum(n))