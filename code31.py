#34.	 Quadrants in which a given lies

x =int(input("Enter the first number:"))
y =int(input("Enter the second number:"))
if(x > 0 and y>0):
    print("first Quadrants")
elif(x < 0 and y>0):
    print("second Quadrant")
elif(x < 0 and y<0):
    print("Third Quadrant")
elif x >0  and  y <0:
    print("Fourth Quadrant")
else:
    print("X and y lie at origin")