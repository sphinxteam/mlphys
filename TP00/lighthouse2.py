from scipy.optimize import brentq

def f(alpha, x):
    return 2 * np.sum((x - alpha) / (beta ** 2 + (x - alpha) ** 2))

ns = range(10,1000)
alphas = [brentq(f, -90, 90, args = samples[:n_samples]) for n_samples in ns]
plt.plot(ns, alphas)
plt.axhline(30, color = "r", lw = 2)
plt.xlabel(r"$N$")
plt.ylabel(r"$\alpha$")