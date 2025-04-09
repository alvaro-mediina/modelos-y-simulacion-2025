"""
Contiene a los generadores de:
    - Von Neumann
        - generator (Method)
        - period (Method)
    - Congruencial Lineal Mixto

    - Congruencial Lineal Multiplicativo
"""

import math
from utils import prime_factor_descomposition


class Von_Neumann:

    @staticmethod
    def generator(n: int) -> int:
        """
        Generador de Von Neumann

        Args:
            n (int): número de iteración

        Returns:
            int: número de la secuencia de Von Neumann
        """
        return (n ** 2 // 100) % 10000

    @staticmethod
    def period(seed: int) -> int:
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
                seed = Von_Neumann.generator(n=seed)
                period += 1
            else:
                repetition = True
        return period


class LinearCongruentialMixed:
    @staticmethod
    def linear_congruential_mixed(self, a: int, c: int, M: int, y_i: int) -> int:
        """
        Generador Congruencial Lineal Mixto

        Args:
            a (int): parámetro del generador congruencial
            c (int): parámetro del generador congruencial
            M (int): cota superior de la secuencia
            y_i (int): valor de la i-ésima iteración

        Returns:
            int: Devuelve la iteración i+1-ésima de la secuencia.
        """
        return (a*y_i+c) % M

    @staticmethod
    def is_maximum_period(a: int, c: int, M: int, ) -> bool:
        """
        Determina si se puede generar una secuencia con periodo máximo

        Args:
            a (int): parámetro del generador congruencial
            c (int): parámetro del generador congruencial
            M (int): cota superior de la secuencia

        Returns:
            bool: True en caso de poder generar un periodo máximo, False en caso contrario.
        """
        prime_descomposition = prime_factor_descomposition(n=M)
        factor_min_prime = min(prime_descomposition)
        is_maximum = False
        if math.gcd(c, M) == 1:
            if a % factor_min_prime == 1:
                if M % 4 == 0 and a % 4 == 1:
                    is_maximum = True
        return is_maximum


class LinearCongruentialMultiplicative:
    @staticmethod
    def linear_congruential_multiplicative(self, a: int, M: int, y_i: int) -> int:
        return (a*y_i) % M

    @staticmethod
    def is_primitive_root(candidate: int, prime_factorization: list[int], M: int) -> bool:
        """
        Determina si el candidato es raíz primitiva de M.

        Args:
            candidate (int): candidato a raíz primitiva.
            prime_factorization (list[int]): factorización prima de M.
            M (int): parámetro del que se quier hallar las raíces primitivas.

        Returns:
            bool: True en caso de ser candidate raíz primitiva de M, False en caso contrario.
        """
        for prime in prime_factorization:
            exp = (M - 1) // prime
            result = pow(candidate, exp, M)
            if result == 1:
                return False
        return True

    @staticmethod
    def root_primitive_candidates(M: int) -> list[int]:
        root_candidates = []
        prime_descomposition = prime_factor_descomposition(n=M-1)
        print(f"Descomposición Prima de {M-1} -> {prime_descomposition}")
        candidate = 1
        while candidate <= M-1:
            is_candidate = LinearCongruentialMultiplicative.is_primitive_root(
                candidate=candidate, prime_factorization=prime_descomposition, M=M)
            if is_candidate:
                root_candidates.append(candidate)
            candidate += 1
        return root_candidates
