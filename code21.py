#  Harshad number

n=int(input("Enter the number "))
sum = 0
temp = n
while(temp >0):
    digit= temp % 10
    sum += digit
    temp //=10
print(sum)

if(n % sum ==0):
    print("this is a Harshad number")
else:
    print("Not")
