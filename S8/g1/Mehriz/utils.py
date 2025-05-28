def is_prime(number):
    lim = int(number ** .5)
    for i in range(2, lim + 1):
        if number % i == 0:
            return False
    return True