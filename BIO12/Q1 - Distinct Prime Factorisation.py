n = int(input(">"))
def isprime(u):
    for i in range(2,u):
        if u % i == 0:
            return False
    return True
tempn =n
factors = []
while tempn > 1:
    lastprime = 2   
    while tempn % lastprime != 0:
        lastprime += 1
        while isprime(lastprime) == False:
            lastprime += 1     
    tempn = tempn / lastprime
    factors.append(lastprime)           
uniquefs = []
for factor in factors:
    if factor not in uniquefs:
        uniquefs.append(factor)
z = 1
for f in uniquefs:
    z *= f
print(str(z))
