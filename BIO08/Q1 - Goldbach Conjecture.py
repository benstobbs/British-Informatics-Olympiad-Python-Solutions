n = int(input(">"))
def genprimes(n):#generate primes from 2 to n
    primes = []
    for i in range(2,n):
        prime = True
        for a in range(2,i):
            #print(str(i) + " / " + str(a))
            if i % a == 0:
                prime = False
        if prime == True:
            primes.append(i)
    return primes

pairs = []
primes = genprimes(n)

for prime1 in primes:
    for prime2 in primes:
        if prime1 + prime2 == n and [prime1,prime2] not in pairs and [prime2,prime1] not in pairs:
            pairs.append([prime1,prime2])
print(len(pairs))
        
