from random import random


class RandomVariables:

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
