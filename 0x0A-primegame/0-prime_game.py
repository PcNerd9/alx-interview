#!/usr/bin/python3

"""
Developed a game, that's played by Maria and Ben
"""


def number_of_prime(n):
    """
    Compute the number of prime number before and including n
    """

    prime = []
    not_prime = []

    for digit in range(2, n + 1):
        if digit not in not_prime:
            prime.append(digit)
        for other_digit in range(digit + 1, n + 1):
            if other_digit % digit == 0 and digit ** 2 >= other_digit:
                not_prime.append(other_digit)

    return len(prime)


def isWinner(x, nums):
    """
    Computer the winner of the game
    """

    players = {
            "Maria": 0,
            "Ben": 0
            }
    for number in nums:
        if number == 0 or number == 1:
            players["Ben"] += 1

        number_prime = number_of_prime(number)
        if number_prime % 2 == 1:
            players["Maria"] += 1
        else:
            players["Ben"] += 1

    if players["Ben"] == players["Maria"]:
        return None
    elif players["Ben"] > players["Maria"]:
        return "Ben"
    else:
        return "Maria"
