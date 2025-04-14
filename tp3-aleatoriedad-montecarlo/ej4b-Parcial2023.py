from random import random
from math import e
from typing import Callable


def function_to_integrate(x: int) -> float:
    return (x ** 3) * (e ** (-x ** 3))


def change_of_variable(x: int, f: Callable[[float], float]) -> float:
    # En este caso h(y) = f(1/y - 2) * 1/(y ** 2)
    y = 1 / x
    integrand = f(y - 2)
    jacobian = (y ** 2)
    h_at_x = integrand * jacobian
    return h_at_x


def monte_carlo(Nsim: int) -> float:
    summation = 0
    for _ in range(Nsim):
        x = random()
        h_at_x = change_of_variable(x=x, f=function_to_integrate)
        summation += h_at_x
    return summation / Nsim


def main():
    print("="*30)
    for Nsim in [1000, 10000, 100000, 1000000]:
        print(f"Nsim:{Nsim:8}  I ≈ {monte_carlo(Nsim=Nsim)}")
    print("="*30)


if __name__ == "__main__":
    main()
