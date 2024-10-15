def nextPrime(prime):
    num = prime[-1]
    while True:
        num += 2  
        count = 0
        isPrime = True
        while num**(1/2) > (cur := prime[count]) and isPrime:
            if num % cur == 0:
                isPrime = False
            count += 1
        if isPrime:
            return num  

def notPrime(p):
    if p == 2:
        return False
    s = 4
    m = 2**p - 1 
    for _ in range(p - 2):
        s = (s * s - 2) % m  
    return not s == 0  

def makePerfectNumber(primes, usedPrimes):
    p = primes[-1]
    while p in usedPrimes or notPrime(p):
        p = nextPrime(primes)
        primes.append(p)
    usedPrimes.add(p)
    print("Value of p:", p)
    return (2**p - 1) * 2**(p - 1)  

count = 1
perfectNumbers = [6]
usedPrimes = {2}

amount = int(input("How many perfect numbers do you want to generate? "))
print("")
print(f"Perfect number NO: {1}")
print("Value of p:", 2)
print("6")
primes = [2, 3]
while count < amount:
    print(f"Perfect number NO: {count + 1}")
    perfectNumbers.append(makePerfectNumber(primes, usedPrimes))  
    print(perfectNumbers[-1]) 
    print("")
    count += 1

ps = []
for i in usedPrimes:
    ps.append(i)
ps.sort()
print("All values of p used:")
for i in ps:
    if i == ps[-1]:
        print(i)
        break
    print(str(i)+", ", end="")
print("")