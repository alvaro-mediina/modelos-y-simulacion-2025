"""
    Este archivo contendrá variables aleatorias de distinto tipo
"""
from random import random


def discret_U(n: int) -> int:
    """
    Variable aleatoria Uniforme Discreta

    Args:
        n (int): cota superior

    Returns:
        int: Probabilidad de que X sea <= 1
    """
    U = random()
    x = 1
    F = 1/n
    while U >= F:
        F = 1 / n
        x += 1
    return x
