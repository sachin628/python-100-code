#Binary to decimal conversion

# num = int(input("Enter the number: "))
# binary_val = num
# decimal_val = 0
# base = 1 
# while num>0:
#     rem= num % 10
#     decimal_val = decimal_val + rem * base
#     num = num // 10
#     base = base * 2
# print("Binary number is {} and Decimal Number is {}".format(binary_val, decimal_val))

#using while Loop

# print("Enter the Binary Number: ")
# bnum = int(input())

# dnum = 0 
# i = 1
# while bnum!=0:
#     rem = bnum%10
#     dnum = dnum +(rem*1)
#     i = i*2
#     bnum = int(bnum/10)
# print("Equivalent decimal Value = ", dnum)

#...............................using for Loop........................................


# print("Enter the Binary Number: ")
# bnum = int(input())
# dnum = 0 
# m = 1
# blen = len(str(bnum))

# for k in range(blen):
#     rem = bnum%10
#     dnum = dnum + (rem * m)
#     m = m * 2
#     bnum = int(bnum/10)
# print("Equivalent decimal = ", dnum)

#...................................................using function.............................


# def decimal(b):
#   return int(b,2)

# print("Enter the Binary Number: ", end="")
# bnum = input()
# dnum = decimal(bnum)
# print("Equivalent Decimal value= ",dnum)  
    
#..........*************************..............using class.........**************

class Sachin:
  def BintoDec(self, b):
    return int(b, 2)

print("Enter the Binary Number : ",end="")
bnum = input()
ob =  Sachin()
dnum = ob.BintoDec(bnum) 
print("Decimal value = ", dnum)