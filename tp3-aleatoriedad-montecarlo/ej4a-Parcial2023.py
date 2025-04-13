from math import e
from random import random
from typing import Callable


def function_to_integrate(x: float) -> float:
    """
    Función a integrar del ejercicio 4a

    Args:
        x (float): entrada

    Returns:
        float: la entrada aplicada a la función
    """
    return x / (x - e ** x)


def change_to_variable(y: float, a: int, b: int, g: Callable[[float], float]) -> float:
    """
    Aplica el cambio de variable para mapear el intervalo [a,b] en [0,1] de la función inicial
    a la función del cambio de variable.

    Args:
        y (float): parámetro de entrada
        a (int): valor inicial del intervalo
        b (int): valor final del intervalo
        g (Callable[[float], float]): Función que toma un flotante y devuelve un flotante

    Returns:
        float: Valor de entrada aplicado a la función de cambio de variable considerando la
        función a integrar.
    """
    # cambio de variable
    # h(y) = g((b-a)y + a)(b-a)
    integrand = g((b-a)*y+a)
    factor = (b-a)
    return integrand * factor


def monte_carlo(Nsim: int, a: int, b=int):
    summation = 0
    for _ in range(Nsim):
        x = random()
        summation += change_to_variable(y=x, a=a, b=b, g=function_to_integrate)
    return summation / Nsim


def main():
    print("="*50)
    for Nsim in [1000, 10000, 100000, 1000000]:
        print(f"n:{Nsim:8} I ≈  {monte_carlo(Nsim=Nsim, a=-3, b=3):.6f}")
    print("="*50)


if __name__ == "__main__":
    main()
