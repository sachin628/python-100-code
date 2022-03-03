#Lowest common Multiply(LCM)

# def compute_lcm(x,y):
#     if x>y:
#         greater = x
#     else:
#         greater = y
#     while(True):
#         if((greater %x == 0) and (greater % y == 0)):
#             lcm = greater 
#             break 
#         greater +=1
#     return lcm

# num1=54
# num2=24

# print("The L.C.M", compute_lcm(num1, num2))

#using GCD 
# This function computes GCD 
def gcd(x, y):
    while(y):
        x, y =y, x % y
    return x
# This function computes LCM
def lcm(x, y):
    lcm = (x*y)//gcd(x,y)
    return lcm
num1 = 54
num2 = 24

print("The LCM is " , lcm(num1,num2))