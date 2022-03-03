#Power of a number

# base_number = int(input("Enter the base number"))
# exponent = int(input("Enter the exponent number "))
# power = base_number ** exponent
# print("Result is = ",power)

#Factor of a number
# def factor(x):
#     print("The factors of ", x , "are:")
#     for i in range(1,x + 1):
#         if x % i == 0:
#             print(i)
# num = 325
# factor(num)


# strong number 
# def factorial(number):
#     if(number == 0 or number == 1):
#         fact = 1
#     else:
#         fact = number * factorial(number - 1)
#     return fact

# def strong_number(list):
#     new_list =[]

#     for x in list :
#         temp = x
#         sum = 0
#         while(temp):
#             rem = temp % 10
#             sum += factorial(rem)
#             temp = temp // 10 
#         if(sum == x):
#             new_list.append(x)
#         else:
#             pass
#     return new_list
# val_list = [1, 2, 5, 145,654,34]
# strong_num_list = strong_number(val_list)
# print(strong_number)

sum1 = 0
num=int(input("Enter a number: "))
temp=num
while(num):
    i=1
    f=1
    r=num%10
    while(i<=r):
        f=f*i
        i=i+1
    sum1=sum1+f
    num=num//10
if(sum1==temp):
    print("the number is a strong number")
else:
    print("not")
