inp = input(">").split(" ")
l,p,q = int(inp[0]),int(inp[1]),int(inp[2])
def genprimes(n): 
    limitn = n+1 
    not_prime = set() 
    primes = [] 
 
    for i in range(2, limitn): 
        if i in not_prime: 
            continue 
        for f in range(i*2, limitn, i): 
            not_prime.add(f) 
        primes.append(i) 
    return primes

primes = genprimes(l)
