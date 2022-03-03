#..........30.	 Decimal to Binary conversion ............

def decimaltobin(num):

    if num >= 1:
        decimaltobin(num // 2)
    print( num % 2, end = '')
dec_val = int(input("enter the value"))
decimaltobin(dec_val)

#............. Decimal to Octal conversion...


         