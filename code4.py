#5.	 Sum of numbers in a given range
n1 = int(input("Enter the lower limit:"))
n2 = int(input("Enter the upper limit:"))
sum = 0
for i in range(n1,n2):
    sum = sum + i
print(sum)

