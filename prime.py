def isprime(x) : #<int>
    """Returns True if the number is prime, False otherwise"""

    x = int(x)

    for val in reversed(range(x + 1)) :
        if val > 1: 
            for n in reversed(range(2, val)): 
                if (val % n) == 0: 
                    return False
            else:
                return True 

def primeGen(n) : #<int>
    """Return the first n prime numbers"""

    n = int(n)

    primeList = []
    num = 2 

    while len(primeList) < n:
        for x in range(2, num): 
            if (num % x) == 0:
                break
        else:
            primeList.append(num)

        num += 1

    return primeList #<list>

def primeSearch(min, max) : # <int> <int>
    """Find prime numbers in a range of numbers
    from min to max """

    min = int(min)
    max = int(max)

    primeList = []

    for val in range(min, max + 1): 

        if val > 1: 

            for n in range(2, val):
                if (val % n) == 0: 
                    break 

            else: 
                primeList.append(val)

    return primeList # <list>

if __name__ == "__main__" :
    print("Is 33 a prime number ? : {}".format(isprime(33)))
    print("Is 13 a prime number ? : {}\n".format(isprime(13)))
    print("The 10 first prime numbers : {}\n".format(primeGen(10)))
    print("Prime numbers between 80 and 100 : {}".format(
        primeSearch(80,100)))