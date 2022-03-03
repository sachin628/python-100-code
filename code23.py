#Friendly pair

n1= int(input("Enter the  First number: "))
n2= int(input("Enter the second number: "))
sum1=0
sum2=0
for i in range(1,n1):
    if(n1%i==0):
        sum1=sum1+i
for i in range(1,n2):
    if(n2%i==0):
        sum2=sum2+i
if sum2==n1 and sum1 == n2:
    print("This is a friendly pair number")
else:
    print("Not")
                                                                                                                                                                                                                                                                   