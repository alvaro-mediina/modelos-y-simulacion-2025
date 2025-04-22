from random import random


"""
Simulación:
    A gana en la primera jugada o en la segunda jugada.
"""


def raffles_simulation() -> str:
    winner = ""
    # Jugada 1 de A
    U = random()
    # Jugada 1 de B
    V = random()
    if U > 0.5 and V < 0.5:
        winner = 'A'
    elif V > 0.5 and U < 0.5:
        winner = 'B'
    else:
        # Jugada 2 de A
        U = random()
        # Jugada 2 de B
        V = random()
        if U > 0.5 and V < 0.5:
            winner = 'A'
        elif V > 0.5 and U < 0.5:
            winner = 'B'
    return winner


def prob_simulation(Nsim: int) -> float:
    games_won_by_A = 0

    for _ in range(Nsim):
        winner = raffles_simulation()
        if winner == 'A':
            games_won_by_A += 1

    return games_won_by_A / Nsim


def main():
    for Nsim in [1000, 10000, 100000, 1000000]:
        print(
            f"Nsim:{Nsim:8}, P(A gana en la primera o segunda partida) = {prob_simulation(Nsim=Nsim):.6}")


if __name__ == '__main__':
    main()
