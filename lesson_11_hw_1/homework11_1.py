from typing import List

def prime_generator(n: int) -> List[int]:
    primes = []
    num = 2
    while num <= n:
        is_prime = True
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            yield num
        num += 1

while True:
    n = int(input("Введіть верхню межу діапазону простих чисел: "))

    prime_nums = list(prime_generator(n))

    print(prime_nums)
