def von_neumann(n:int) -> int:
    return (n ** 2 // 100) % 10000


def von_neumann_period(seed:int) -> int:
    period = 0
    secuence = []
    repetition = False
    while not repetition:
        if not seed in secuence:
            secuence.append(seed)
            seed = von_neumann(seed)
            period+=1
        else:
            repetition = True
    return period

def main():
    seeds = [3009, 7600, 1234, 4321]
    for seed in seeds:
        period = von_neumann_period(seed=seed)
        print(f"El periodo de la semilla [{seed}] es -> {period}")
        



if __name__ == "__main__":
    main()