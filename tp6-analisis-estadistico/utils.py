import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# pi_numbers_for_iteration:list[float]
#[0] -> 1000 iteraciones
#[1] -> 10000 iteraciones
#[2] -> 100000 iteraciones
#[3] -> 1000000 iteraciones
#[4] -> 10000000 iteraciones

pallete = sns.color_palette("magma")
pallete1 = sns.color_palette("mako")

COLORS_HEX = [
    pallete[0],  
    pallete[1],
    pallete[2],  
    pallete[3],  
    pallete[4],  
    pallete[5],   
    pallete1[0],  
    pallete1[1],  
    pallete1[2],  
    pallete1[3]    
]


def map_colors_in_number(numbers: list[float]) -> list:
    color = []
    rng = np.random.default_rng()
    for _ in numbers:
        color_selected = rng.choice(COLORS_HEX)
        color.append(color_selected)
    return color



def pi_graphic(pi_numbers:list[tuple[float, float]]):
    # Gráfico
    fig, ax = plt.subplots(figsize=(6, 6))

    circle = plt.Circle((0, 0), 1, fill=False, color='black', linestyle='-', linewidth=2)
    ax.add_patch(circle)

    iterations = len(pi_numbers)

    x_vals = [x for x, y in pi_numbers]
    y_vals = [y for x, y in pi_numbers]

    colors:list[str] = map_colors_in_number(x_vals)

    ax.scatter(x_vals, y_vals, color=colors, s=20, alpha=1, label='Puntos dentro del círculo')

    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)

    ax.grid(True, linestyle='--', alpha=0.7)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)

    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_title(f'Aproximación de π con {iterations} puntos')


    plt.axis('equal')  # Para que la escala en X e Y sea igual (evita deformación)
    plt.show()



