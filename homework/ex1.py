import random
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt


# *** 1 ***

def calc_final_pos(init_pos: int, p_forward: float, n_steps: int) -> int:
    """
    Computes the final position of the walker after
    `n_steps`, given the probability to move forward
    `p_forward`.

    Args:
        init_pos:  Initial position of the walker
        p_forward: Probability to move forward
        n_steps:   Number of steps to compute
    
    Returns:
        final_pos: Final position after `n_steps` steps

    """

    final_pos = init_pos

    for step in range(n_steps):
        if random.random() < p_forward:
            # move forward
            final_pos += 1
        else:
            # move backward
            final_pos -= 1
    
    return final_pos


# *** 2 ***

# the expected final position for p=0.5 is the initial position

n_experiments = 10000
final_positions = []

for n in range(n_experiments):
    final_positions.append(calc_final_pos(0, 0.5, 1000))

PART = 4

# *** 3 ***

if PART == 3:
    plt.hist(final_positions, bins=np.unique(final_positions))

    sigma_exp = np.std(final_positions)

    mu = 0
    sigma = sigma_exp
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    plt.plot(x, 19500*np.array(stats.norm.pdf(x, mu, sigma)), linewidth=4, label=f"Gaussian with mu={0} and std={sigma:.2f}")
    plt.legend()
    plt.show()


# *** 4 ***
if PART == 4:

    final_positions = []
    n_steps = [20, 50, 100, 200, 1000, 50000]

    for n_st in n_steps:
        for n in range(n_experiments):
            final_positions.append(calc_final_pos(0, 0.5, n_st))

        plt.hist(final_positions, bins=np.unique(final_positions), normed=1)

        sigma_exp = np.std(final_positions)
        print(f"N = {n_st}: sigma = {sigma_exp:.2f} ({np.log(n_st):.2f})")

        mu = 0
        sigma = sigma_exp
        x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
        plt.plot(x, np.array(stats.norm.pdf(x, mu, sigma)),
                linewidth=4, label=f"Gaussian with mu={0} and std={sigma:.2f}")
        plt.legend()
        plt.savefig(f"plots/ex1_{n_st}_steps.png")
        plt.clf()


# *** 5 ***
if PART == 5:

    n_experiments = 10000
    final_positions = []

    for n in range(n_experiments):
        final_positions.append(calc_final_pos(0, 0.75, 1000))

    sigma_exp = np.std(final_positions)
    print(f"N = {n_experiments}: sigma = {sigma_exp:.2f}")

    plt.hist(final_positions, bins=np.unique(final_positions), normed=1)
    plt.savefig(f"plots/ex1_p_75_steps.png")
    plt.clf()