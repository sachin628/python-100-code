# Replace all zeros with one in a given integers

def reverseThenumber(temp):
    ans = 0
    while (temp >0):
        rem = temp % 10
        ans = ans * 10 +rem
        temp = temp // 10

    return ans
def convert0to1(num):
    if(num == 0 ):
        return 5 
    else:
        temp = 0
        while(num > 0) :
            digit  = num % 10
            if (digit == 0 ):
                digit  = 1
            temp = temp *10 + digit
            num = num // 10 
        return reverseThenumber(temp)
num = 10122
print(convert0to1(num))
        



