import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("outputs.txt")
mean_val = np.mean(data)
std_val = np.std(data)

plt.figure(figsize=(9, 5))
plt.hist(
    data, bins=80, density=True, color="#008080", alpha=0.75, edgecolor="white"
)

plt.axvline(
    mean_val,
    color="red",
    linestyle="--",
    linewidth=2,
    label=f"Mean: {mean_val:.2f} g/cm³",
)
plt.axvline(
    mean_val - std_val,
    color="orange",
    linestyle=":",
    linewidth=2,
    label=f"1-sigma: ±{std_val:.2f}",
)
plt.axvline(mean_val + std_val, color="orange", linestyle=":", linewidth=2)

plt.xlabel("Bulk Density (g/cm³)", fontsize=12)
plt.ylabel("Probability Density", fontsize=12)
plt.title(
    "TRAPPIST-1b Monte Carlo Density Distribution (n = 100,000)", fontsize=13
)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)

plt.show()