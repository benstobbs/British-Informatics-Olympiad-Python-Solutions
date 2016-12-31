inp = input(">").split(" ")
n = int(inp[2])
alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
a = alpha.index(inp[0])+1
b = alpha.index(inp[1])+1

for i in range(0,n-1):
    a,b = b,a+b
    while a > 26:
        a -= 26
    while b > 26:
        b -= 26
    
print(alpha[a-1])
