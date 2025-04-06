from random import random
from math import exp

def g(u: int) -> int:
    return 2 * exp((2*u - 1) + ((2*u-1) ** 2))

def MonteCarlo(g, NSim) -> int:
    integral = 0
    for _ in range(NSim):
        u_i= random()
        integral += g(u_i)
    return integral/NSim

def main():
    NSim = int(input("Ingresar cantidad de simulaciones ->"))
    print(f"Valor de la integral: {MonteCarlo(g, NSim)}")

if __name__ == '__main__':
    main()