import time

def is_prime(number):
    if number < 2:
        return False

    lim = int(number ** .5) + 1
    for i in range(2, lim):
        if number % i == 0:
            return False

    return True
    
def primes_less_than(number):
    for i in range(number+1):
        if is_prime(i) == True:
            time.sleep(1)
            yield i


for x in primes_less_than(100):
    print(x)
