import numpy as np


def dirac_eigenvalues(R, eps=(0.5, 0.5, 0.5), cutoff=5):
    """Compute positive Dirac eigenvalue magnitudes on T^3."""
    R1, R2, R3 = R
    e1, e2, e3 = eps
    vals = []

    for n1 in range(-cutoff, cutoff + 1):
        for n2 in range(-cutoff, cutoff + 1):
            for n3 in range(-cutoff, cutoff + 1):
                k2 = (
                    ((n1 + e1) / R1) ** 2
                    + ((n2 + e2) / R2) ** 2
                    + ((n3 + e3) / R3) ** 2
                )
                vals.append(2 * np.pi * np.sqrt(k2))

    return np.array(vals)


def count_states(R, Lambda=1.0, eps=(0.5, 0.5, 0.5), cutoff=10):
    """Count eigenvalues satisfying mu^2 < Lambda^2."""
    mus = dirac_eigenvalues(R, eps=eps, cutoff=cutoff)
    return int(np.sum(mus**2 < Lambda**2))
