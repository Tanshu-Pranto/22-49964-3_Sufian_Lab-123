import math

limit = 1000

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd factors up to the square root of n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# Renamed 'sum' to 'prime_sum' to avoid shadowing Python's built-in sum() function
prime_sum = 0 

for i in range(2, limit + 1):
    if is_prime(i):
        prime_sum += i

print(prime_sum)