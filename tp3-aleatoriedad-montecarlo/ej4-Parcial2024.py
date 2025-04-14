from random import random
from math import log
from typing import Callable
from monte_carlo import MonteCarlo


def monte_carlo_1_inf(Nsim: int) -> float:
    summation = 0
    for _ in range(Nsim):
        x = random()
        y = 1.0 / x
        integrand = function_to_integrate(y)
        jacobian = 1 / (x ** 2)
        summation += integrand * jacobian
    return summation / Nsim


def function_to_integrate(x: float) -> float:
    denominator = (x ** 2) * log(x+1)
    return 1.0 / denominator


def main():
    print("="*30)
    for n in [1000, 10000, 100000]:
        print(f"n:{n:8} I ~ {monte_carlo_1_inf(Nsim=n):.6f}")
    print("="*30+"\n")


if __name__ == '__main__':
    main()
