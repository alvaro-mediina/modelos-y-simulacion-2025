from generators import Von_Neumann


def main():
    """
    --------------
    Ejercicio 1 A
    --------------
    """
    seeds = [3009, 7600, 1234, 4321]
    for seed in seeds:
        period = Von_Neumann.period(seed=seed)
        print(f"El periodo de la semilla [{seed}] es -> {period}")


if __name__ == '__main__':
    main()
