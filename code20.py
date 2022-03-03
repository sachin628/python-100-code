#Automorphic number

num =int(input("Enter the number you want to check"))
num_of_digits=len(str(num))
square=num **2
last_digits=square%pow(10,num_of_digits)
if last_digits==num:
    print("yes,{} is an automporphic number".format(num))
else:
    print("Not")