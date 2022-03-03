# Maximum number of handshakes...

# N = int(input("Enter number of people available:"))
# # formula
# no_of_handshake = int(N * ((N - 1)/2))
# print("Maximumnumber of handshake can be : " + str(no_of_handshake))

#.......................using function...................

def maxHandshake(n):
    return int((n * (n - 1))/2)
n = 10 
print(maxHandshake(n))