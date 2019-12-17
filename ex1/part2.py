import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 4, figsize=(4*5, 5))

for n in range(1, 5):
    print(f"case {n}:")

    # read data
    with open(f"case{n}.txt") as f:
        data = np.fromstring(f.read(), dtype=float, sep='\n')

    # Shapiro-Wilk test
    _, p = stats.shapiro(data)
    print(f"Shapiro-Wilk test p-value: {p:.3f}")

    # mean and std
    mean, std = data.mean(), data.std()
    print(f"mean: {mean:.3f}")
    print(f"std: {std:.3f}")

    # plot the distribution
    axs[n-1].hist(data, bins=10)

    print()

plt.show()