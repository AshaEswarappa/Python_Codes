def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

def listprimes(N):
    
    for n in range(N):
        if isprime(n):
            print(n, end = ' ', flush = True)
    
N = int(input("Enter the range of numbers to check: "))
print("The list of prime numbers in the range of {} are: ".format(N))

listprimes(N)