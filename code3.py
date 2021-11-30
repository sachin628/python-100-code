#Sum of First N Natural numbers
# n = int(input("Enter the number:"))
# if n>=0:
#  sum =0
#  for i in range(n+1):
#     sum = sum + i
#  print(sum)
# else:
#     print("the number is not natural") 



    ####################### Another method ######
n=int(input("Enter a number: "))
sum1 = 0
while(n > 0):
    sum1=sum1+n
    n=n-1
print("The sum of first n natural numbers is",sum1)

