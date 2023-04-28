import math
def num_prime(num):
    if num < 2:
        return False
    for digit in range(2, int(math.sqrt(num))+1):
        if num % digit == 0:
            return False
    return True

for digit in range(2, 1001):
    if num_prime(digit):
        print(digit)
