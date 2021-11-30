#Even or Odd number
num = int(input("Enter the range:"))
for i in range(num):
    n = int(input("Enter the valid number:"))
    if n%2==0:
      print("the number is even")
    else:
      print("The number is odd")