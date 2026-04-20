import numpy as np
import matplotlib.pyplot as plt

# Parameters
r_s = 1.0                  # Schwarzschild radius
G = 1.0
Lambda = 0.01              # positive cosmological constant
alpha = (8 * np.pi * G / 3) * Lambda

# Effective potential for radial timelike geodesics
def V_eff(r):
    return 1 - r_s / r - alpha * r**2

# Domain: avoid r=0
r = np.linspace(0.05, 8.0, 2000)
V = V_eff(r)

# Location of the maximum
r_max = (r_s / (2 * alpha))**(1/3)
V_max = V_eff(r_max)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(r, V, label=r"$V_{\rm eff}(r)=1-\frac{r_s}{r}-\alpha r^2$")
plt.axvline(r_max, linestyle="--", label=rf"$r_{{\max}}={r_max:.3f}$")
plt.plot(r_max, V_max, "o")

plt.xlabel(r"$r$")
plt.ylabel(r"$V_{\rm eff}(r)$")
plt.title("Schwarzschild-de Sitter Effective Potential for Massive Radial Geodesics")
plt.xlim(r.min(), r.max())
plt.ylim(-10, 2)
plt.grid(True)
plt.legend()
plt.show()