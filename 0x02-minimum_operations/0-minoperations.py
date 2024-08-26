#!/usr/bin/python3

"""
contains two functions:
    1. Compute_next_prime_no: takes a single parameter
        which then compute the next prime number
    2. minOperaion: takes a single parameter whch return
        the min operation taken to get to the input number
"""


def compute_next_prime_no(prime_n):
    """
    compute the next prime no
    """
    next_prime_n = prime_n
    found_prime_n = 0
    while not found_prime_n:
        next_prime_n += 2
        count = 2
        not_prime = 0
        while count < next_prime_n:
            if next_prime_n % count == 0:
                not_prime = 1
                break
            count += 1
        if not not_prime:
            return next_prime_n


def minOperations(n):
    """
    compute the minimum operation that needs
    to be performed to get to n
    """
    prime_numbers = [2, 3]
    divisor = n
    prime_factors = []
    while not (divisor <= 1):
        dividable = 0
        for prime in prime_numbers:
            if divisor % prime == 0:
                prime_factors.append(prime)
                dividable = 1
                divisor = divisor / prime
                break
        if not dividable:
            new_prime = compute_next_prime_no(prime_numbers[-1])
            prime_numbers.append(new_prime)
            if divisor % new_prime == 0:
                prime_factors.append(new_prime)
                divisor = divisor / new_prime
    return sum(prime_factors)
