#Permutation in which n people can occupy ‘r ‘ seats in a class room
import math
N = int(input("Enter the number of students : "))

R = int(input("Enter the number of seats : "))
nume = math.factorial(N)
deno = math.factorial(N-R)
# permutation = n! /(n - r)!

no_of_ways = nume // deno
print("Totasl number of ways are : " + str(no_of_ways))