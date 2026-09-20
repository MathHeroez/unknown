import numpy as np
from dirac_t3 import count_states


def search_best_ratio(Lambda=10, steps=20):
    """Search for the lowest state count among unit-volume radius triples."""
    best = None
    best_R = None

    for r1 in np.linspace(0.5, 2.5, steps):
        for r2 in np.linspace(0.5, 2.5, steps):
            r3 = 1.0 / (r1 * r2)
            if r3 < 0.5 or r3 > 2.5:
                continue

            R = (r1, r2, r3)
            N = count_states(R, Lambda=Lambda, cutoff=15)
            if best is None or N < best:
                best = N
                best_R = R

    return best_R, best


if __name__ == "__main__":
    R_opt, N_opt = search_best_ratio(Lambda=12, steps=25)
    print(f"Optimal R (vol=1): {R_opt}")
    print(f"Ratios: R2/R1={R_opt[1] / R_opt[0]:.3f}, R3/R1={R_opt[2] / R_opt[0]:.3f}")
    print(f"Target sqrt(3/2)={np.sqrt(3/2):.3f}, sqrt(5/2)={np.sqrt(5/2):.3f}")
    print(f"Min N: {N_opt}")

    R_k = (np.sqrt(2), np.sqrt(3), np.sqrt(5))
    R_k = tuple(r / (np.prod(R_k) ** (1/3)) for r in R_k)
    print(f"\nCandidate K ratio N: {count_states(R_k, Lambda=12, cutoff=15)}")
