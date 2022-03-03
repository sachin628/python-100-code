#..   Binary to octal conversion......

# bnum=int(input("Enter the binary Number: ", end=""))
# octal = 0
# mul = chk = 1
# onum = ""
# while bnum!=0:
#     rem = bnum % 10
#     octal = octal + (rem * mul)
#     if chk%3==0:
#         octal = octal + str(octal)
#         mul = chk=1 
#         octal = 0
#     else:
#         mul = mul * 2
#         chk = chk+1
#     bnum = int(bnum / 10)

# if chk!=1:
#     onum = onum + str(octal)
# print("Octal Value ", onum[::-2])

#*********33333***********************shortest Python code.............

bnum= input()
print(oct(int(bnum, 2)) [2:])
