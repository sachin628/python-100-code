#Abundant number

n= int(input("Enter the number: "))
sum = 0
#temp = n
for i in range(1,n):
    if(n%i==0):
        sum=sum+i

    # if(temp % i == 0):
    #     sum1 = sum1 +i
if(sum > n):
    print("This is a Abundant number")
else:
    print("Not")