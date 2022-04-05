import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """
    r^2 = (x-0.4)^2 + (y+0.4)^2
    r^2 - (x-0.4)^2 = (y+0.4)^2
    sqrt(r^2 - (x-0.4)^2) = y + 0.4
    y = sqrt(r^2 - (x-0.4)^2) - 0.4
    """
    return np.sqrt(5 - (x-0.4)**2) - 0.4

def luasmc(f, a, b, N):
    y = f(np.random.uniform(a, b, N))
    return np.sum(y) / (N-1) * (b-a)

# jawaban
true_val = 3.33277

Ns = np.arange(10, 10000, 20)
all_error = []
for N in Ns:
    luas = luasmc(f, 0, 2, N)
    error = abs(true_val - luas)
    all_error.append(error)

plt.plot(Ns, all_error)
plt.axhline(0, c='r')
plt.grid()
plt.xlabel('Number of samples')
plt.ylabel('Absolute error')
plt.show()

