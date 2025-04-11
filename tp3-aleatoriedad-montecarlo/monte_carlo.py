from random import random
from typing import Callable


class MonteCarlo:
    @staticmethod
    def log(real_result: float, aproximations: list[float], iterations: list[int]):
        print(f"[VALOR REAL] -> {real_result}\n")
        if len(aproximations) != len(iterations):
            raise ValueError(
                "Las listas 'aproximations' e 'iterations' deben tener la misma longitud.")

        for i in range(len(iterations)):
            print(
                f"[APROXIMACIÓN] con [{iterations[i]} ITERACIONES] ~ {aproximations[i]}")
            print(f"[ERROR] {abs(aproximations[i] - real_result)}\n")

    @staticmethod
    def multi_log(real_result: float, aproximations: list[float], iterations: list[int]):

    @staticmethod
    def integral_montecarlo_0_1(f: Callable[[int], float], N: int) -> float:
        integral = 0
        for _ in range(N):
            U = random()
            integral += f(U)
        return integral/N

    @staticmethod
    def integral_montecarlo_a_b(a: int, b: int, g: Callable[[float], float], N: int) -> float:
        integral = 0
        for _ in range(N):
            U = random()
            integral += g(a + (b-a) * U)

        return (integral * (b - a)) / N

    @staticmethod
    def integral_montecarlo_0_plusInf(f, N) -> float:
        integral = 0
        for i in range(N):
            U = random()
            integral += f(1/U - 1) / U**2
        return integral / N

    @staticmethod
    def integral_montecarlo_minusInf_plusInf(f, N) -> float:
        return 2 * MonteCarlo.integral_montecarlo_0_plusInf(f, N)

    @staticmethod
    def integral_montecarlo_0_1_n_vars(g, n_vars: int, N: int):
        integral = 0
        for _ in range(N):
            U_list = [random() for _ in range(n_vars)]
            integral += g(*U_list)

        return integral / N

    @staticmethod
    def integral_montecarlo_0_plusInf_n_vars(g, n_vars: int, N: int):
        integral = 0
        for _ in range(N):
            U_list = [random() for _ in range(n_vars)]
            variable_change = [(1/u - 1) for u in U_list]
            denominator = 1
            for u in U_list:
                denominator *= u**2
            integral += g(*variable_change) / denominator
        return integral / N
