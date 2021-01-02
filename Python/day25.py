import math
import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


with open('Python/input.txt') as file:
    data = file.readlines()
    nums = [int(num.strip()) for num in data]
    nums = nums[1:]

for num in nums:
    if is_prime(num):
        print('Prime')
    else:
        print('Not prime')