from math import sqrt
from typing import Callable
from random import random

"""Ejercicio 1"""


def function_to_integrate(x: int) -> float:
    """
    Función a integrar especificada en el parcial.

    Args:
        x (int): parámetro de entrada

    Returns:
        float: el valor de entrada aplicado a la función
    """
    internal_value = x + sqrt(x)  # x + \/x
    return sqrt(internal_value)  # \/internal_value


def change_of_variable(f: Callable[[int], float], a: int, b: int, y: int) -> float:
    """
    Función h(y) de cambio de variable

    Args:
        f (Callable[[int], float]): Función a integrar, toma un entero, le aplica la función
          y devuelve un flotante.
        a (int): límite de integración inferior
        b (int): límite de integración superior
        y (int): parámetro de entrada a evaluar

    Returns:
        float: _description_
    """
    # cambio de variable
    # h(y) = f((b-a)y + a)(b-a)
    integrand = f((b-a)*y+a)
    factor = (b-a)
    return integrand * factor


def monte_carlo(Nsim: int) -> float:
    """
    Estimación por Monte Carlo

    Args:
        Nsim (int): Número de simulaciones

    Returns:
        float: Estimación
    """
    summation = 0
    for _ in range(Nsim):
        U = random()
        summation += change_of_variable(f=function_to_integrate, a=1, b=7, y=U)
    return summation / Nsim


"""Ejercicio 2"""


def is_uneven(x: int) -> bool:
    return x % 2 == 1


def juego() -> int:
    """
    Genera una sucesión de números aleatorios entre 0 y 1 y los suma hasta que
    la suma sea mayor que 1.

    Returns:
        int: Devuelve el número de sumandos generados.
    """
    accum = 0
    summations = 0

    while not accum > 1:
        # Genero  números aleatorios y los acumulo
        U = random()
        accum += U
        summations += 1

    return summations


def pares(Nsim: int) -> float:
    """
    Cálculo de la probabilidad de que el número de sumados en el juego sea impar

    Args:
    Nsim (int): Número de simulaciones

    Returns:
      int: Probabilidad de que el número de sumados sea impar
    """
    probability = 0
    for _ in range(Nsim):
        if is_uneven(juego()):
            probability += 1
    return probability / Nsim


"""Función Principal"""


def main():

    print("\n")
    print("="*23 + " Ejercicio 1 " + "="*22)
    for Nsim in [1000, 10000, 100000]:
        print(f"N:{Nsim:8} | I ≈ {monte_carlo(Nsim=Nsim):.8}")
    print("="*58)

    print("\n")

    print("="*23 + " Ejercicio 2 " + "="*22)
    attemps = 0
    for Nsim in [100, 1000, 10000]:
        print(
            f"N:{Nsim:8} | P(Num. Tot. de Sumados es Impar) = {pares(Nsim=Nsim):4}")
    print("="*58)


if __name__ == "__main__":
    main()
