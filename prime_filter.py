# Find prime numbers using the in-build method filter 

nums = range(1,100)

def is_prime(num):
    for x in range(2, num):
        if (num%x) == 0:
            return False
        else:
            return True
           
primes = list(filter(is_prime, nums))

print(primes)
