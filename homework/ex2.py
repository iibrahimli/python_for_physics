import random
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt


# *** 1 ***

def step(molecules, p_stay, n_steps, lat_shape=(20, 20)):
    """
    Computes the position of molecules after `n_steps` steps

    Args:
        molecules: Positions of the molecules
        p_stay:    The probability of a molecule to stay in the same cell
        n_steps:   Number of steps to simulate
        lat_shape: The size of the lattice (X, Y)
    
    Returns:
        r_mol:     Result positions of molecules

    """

    r_mol = []

    for step in range(n_steps):
        for mol in molecules:
            rnd = random.random()
            if rnd < p_stay:
                # stay in the same cell
                r_mol.append(mol)
            else:
                if mol[0] == 0 or mol[]
                # top left corner:


    return r_lat


# *** 2 ***