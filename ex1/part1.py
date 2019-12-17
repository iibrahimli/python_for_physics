import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

N_POINTS = 1000

# --- 1 ---
x = stats.norm.rvs   (loc=1,  scale=2, size=N_POINTS)
y = stats.uniform.rvs(loc=-1, scale=2, size=N_POINTS)
z = stats.expon.rvs  (loc=4,           size=N_POINTS)

# --- 2 ---
print(f"x: mean = {x.mean():.3f}, std = {x.std():.3f}")
print(f"y: mean = {y.mean():.3f}, std = {y.std():.3f}")
print(f"z: mean = {z.mean():.3f}, std = {z.std():.3f}")

# --- 3 ---
_, px = stats.shapiro(x)
_, py = stats.shapiro(y)
_, pz = stats.shapiro(z)

print("Shapiro-Wilk test results (p-value)")
print(f"x: {px:.2f}, y: {py:.2f}, z: {pz:.2f}")

# --- 4 ---
# fig, axs = plt.subplots(1, 3, figsize=(3*5, 5))
# axs[0].hist(x, bins=50)
# axs[1].hist(y, bins=50)
# axs[2].hist(z, bins=50)
# plt.show()