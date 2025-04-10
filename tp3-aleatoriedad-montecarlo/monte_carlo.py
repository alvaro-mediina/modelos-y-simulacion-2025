from random import random


class MonteCarlo:
    @staticmethod
    def integral_montecarlo_0_inf(f, N) -> int:
        sum = 0
        for i in range(N):
            U = random()
            sum += f(1/U - 1) / U**2
        return sum / N
