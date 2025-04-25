from random import random
from math import sqrt


class Utils:

    @staticmethod
    def numbers_between_a_b(a: int, b: int) -> int:
        """
        Genera números aleatorios entre a y b

        Args:
            a (int): Límite inferior
            b (int): Límite superior

        Returns:
            int: Número aleatorio entre a y b
        """
        U = random()
        return int(U * (b - a + 1)) + a

    @staticmethod
    def mean_value(numbers: list) -> float:
        """
        Valor medio de una lista de números

        Args:
            numbers (list): Lista de números

        Returns:
            float: Valor medio de la lista
        """
        summation: float = sum(n for n in numbers)
        return summation / len(numbers)

    @staticmethod
    def standar_deviation(numbers: list) -> float:
        """
        Desviación estándar de una lista de números

        Args:
            numbres (list): Lista de números

        Returns:
            float: Valor de la desviación estándar de la lista
        """
        mean: float = Utils.mean_value(numbers=numbers)
        summation: float = sum(
            list(map(lambda x_i: (x_i-mean) ** 2, numbers))) / len(numbers)
        return round(sqrt(summation), 4)
