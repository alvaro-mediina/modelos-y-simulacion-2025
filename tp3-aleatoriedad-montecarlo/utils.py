"""
    Funciones Matemáticas útiles para el lab
"""


def prime_factor_descomposition(n: int) -> list[int]:
    """
    Realiza la descomposición en factores primos de un número entero positivo.

    Args:
        n (int): Número a descomponer (debe ser > 0).

    Returns:
        list[int]: Lista de factores primos en orden creciente.

    Raises:
        ValueError: Si n no es un entero positivo.
    """
    if n <= 0:
        raise ValueError("El número debe ser positivo.")

    prime_factor_list = []

    # Procesar el factor 2 por separado
    while n % 2 == 0:
        prime_factor_list.append(2)
        n = n // 2

    # Procesar factores impares desde 3
    factor = 3
    while n > 1:
        # Solo probar divisores primos
        if is_cousin(n=factor):
            while n % factor == 0:
                prime_factor_list.append(factor)
                n = n // factor
        factor += 2

    return prime_factor_list


def is_cousin(n: int) -> bool:
    """
    Determina si n es un número primo

    Args:
        n (int): número a determinar si es primo

    Returns:
        bool: True en caso de ser primo, False en caso contrario.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    cousin = True
    i = 5
    while i * i <= n and cousin:
        if n % i == 0 or n % (i + 2) == 0:
            cousin = False
        i += 6
    return cousin
