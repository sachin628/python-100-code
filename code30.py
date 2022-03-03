# Octal to Binary conversion.....

import math
def octal_to_binary(octal):
    decimal = 0
    i =0
    binary = 0
    while(octal!=0):
        decimal +=(octal%10)*math.pow(8,i)
        i = i +1
        octal=int(octal/10)
