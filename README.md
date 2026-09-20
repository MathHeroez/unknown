# unknown import numpy as np

def dirac_eigenvalues(R, eps=(0.5,0.5,0.5), cutoff=5):
    """
    D_T3 with variable radii R = (R1,R2,R3)
    mu = 2*pi * sqrt( sum (n_i+eps_i)^2 / R_i^2 )
    """
    R1,R2,R3 = R
    e1,e2,e3 = eps
    vals = []
    for n1 in range(-cutoff, cutoff+1):
        for n2 in range(-cutoff, cutoff+1):
            for n3 in range(-cutoff, cutoff+1):
                k2 = ((n1+e1)/R1)**2 + ((n2+e2)/R2)**2 + ((n3+e3)/R3)**2
                mu = 2*np.pi * np.sqrt(k2)
                vals.append(mu)
    return np.array(vals)

def count_states(R, Lambda=1.0, eps=(0.5,0.5,0.5), cutoff=10):
    mus = dirac_eigenvalues(R, eps, cutoff)
    return np.sum(mus**2 < Lambda**2)

# Compiler test: does sqrt2:sqrt3:sqrt5 minimize N(R) ?
if __name__ == "__main__":
    R_test = (np.sqrt(2), np.sqrt(3), np.sqrt(5))
    # normalize volume to 1 for fair comparison
    R_test = tuple(r / (np.prod(R_test)**(1/3)) for r in R_test)
    R_equal = (1,1,1)
    
    print("R sqrt(2,3,5) normalized:", R_test, "N:", count_states(R_test, Lambda=10))
    print("R equal:", R_equal, "N:", count_states(R_equal, Lambda=10))
