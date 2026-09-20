import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from dirac_t3 import count_states


def search_grid(Lambda=12, steps=25):
    grid = np.linspace(0.5, 2.5, steps)
    counts = np.zeros((steps, steps))
    positions = []

    for i, r1 in enumerate(grid):
        for j, r2 in enumerate(grid):
            r3 = 1.0 / (r1 * r2)
            if r3 < 0.5 or r3 > 2.5:
                counts[i, j] = np.nan
                continue
            R = (r1, r2, r3)
            counts[i, j] = count_states(R, Lambda=Lambda, cutoff=15)
            positions.append((r1, r2, counts[i, j]))

    best = min((c, (r1, r2)) for (r1, r2, c) in positions if not np.isnan(c))
    return grid, counts, best


if __name__ == "__main__":
    grid, counts, best = search_grid(Lambda=12, steps=25)
    min_count, (best_r1, best_r2) = best

    fig, ax = plt.subplots(figsize=(8, 7))
    mesh = ax.imshow(
        counts,
        origin="lower",
        extent=[grid[0], grid[-1], grid[0], grid[-1]],
        cmap="viridis",
        aspect="auto",
    )
    ax.scatter([best_r1], [best_r2], color="red", s=40, label="minimum")
    ax.set_title("State count N(R) over radius grid")
    ax.set_xlabel("R1")
    ax.set_ylabel("R2")
    ax.legend(loc="best")
    fig.colorbar(mesh, ax=ax, label="N(R)")

    print(f"Best grid point: R1={best_r1:.3f}, R2={best_r2:.3f}, N={min_count}")
    print("Saving plot to spectral_search.png")
    fig.tight_layout()
    fig.savefig("spectral_search.png", dpi=200)
    plt.close(fig)
