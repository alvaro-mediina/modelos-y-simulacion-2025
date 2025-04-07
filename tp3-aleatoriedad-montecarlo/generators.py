"""
Contiene a los generadores de:
    - Von Neumann
        - generator (Method)
        - period (Method)
    - Congruencial Lineal Mixto

    - Congruencial Lineal Multiplicativo
"""


class Von_Neumann:
    def generator(self, n: int) -> int:
        """
        Generador de Von Neumann

        Args:
            n (int): número de iteración

        Returns:
            int: número de la secuencia de Von Neumann
        """
        return (n ** 2 // 100) % 10000

    def period(self, seed: int) -> int:
        """
        Calcula el periodo de la secuencia de Von Neumann

        Args:
            seed (int): Semilla

        Returns:
            int: Periodo de la secuencia de Von Neumann
        """
        period = 0
        secuence = []
        repetition = False
        while not repetition:
            if not seed in secuence:
                secuence.append(seed)
                seed = self.generator(seed)
                period += 1
            else:
                repetition = True
        return period


class LinearCongruentialMixed:
    def linear_congruential_mixed(self, a: int, c: int, M: int, y_i: int) -> int:
        return (a*y_i+c) % M


class LinearCongruentialMultiplicative:
    def linear_congruential_multiplicative(self, a: int, M: int, y_i: int) -> int:
        return (a*y_i) % M
