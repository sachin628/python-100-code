#....Decimal to Octal conversion

def dectooctal(n):
    #array to store octal number
    octalNum = 0
    i = 1
    while (n!= 0):
        #storing remainder
        octalNum =   octalNum+(n % 8)*i
        n = int(n / 8)
        i = i * 10
    return octalNum
n = int(input("Enteer the Number:"))
print("Equivalent octal number:",dectooctal(n))

