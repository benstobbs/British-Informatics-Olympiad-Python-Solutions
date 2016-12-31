n = int(input(">"))
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

nos=0
primes = genprimes(n)

for prime in primes:
    if n-prime in primes:
        nos += 1
print(str(int((nos/2)+0.5)))
        
