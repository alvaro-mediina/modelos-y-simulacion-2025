"""
    Funciones Matemáticas útiles para el lab
"""


def prime_factor_descomposition(n: int) -> list[int]:
    prime_factor_list = []

    if n <= 0:
        raise ValueError("El número debe ser positivo.")
    # Divisor 2 (factores pares)
    while n % 2 == 0:
        prime_factor_list.append(2)
        n = n // 2

    # Divisores impares desde 3 hasta √n
    """
        (Teorema de la factorización prima)
        Un número n no es primo => 
        al menos uno de sus factores debe ser menor o igual a √n.
    """
    i = 3
    while i * i <= n:  # Equivalente a i <= √n
        while n % i == 0:
            prime_factor_list.append(i)
            n = n // i
        i += 2

    # Si queda un número primo mayor que 2
    if n > 1:
        prime_factor_list.append(n)

    return prime_factor_list
