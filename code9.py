# #Sum of  digits of a number
# n=int(input("Enter the digit:"))
# sum=0
# while (n != 0):
#     sum = sum +(n%10)
#     n = n//10
# print(sum)

#function to get sum of digits
#def getSum(n):

#     sum = 0
#     for digit in str(n):
#         sum += int(digit)
#     return sum
# n = int(input("Enter the number:"))
# print(getSum(n))

def getSum(n):
    strr = str(n)
    list_of_number = list(map(int, strr.strip()))
    return sum(list_of_number)
n = int(input("Enter the number:"))
print(getSum(n))
