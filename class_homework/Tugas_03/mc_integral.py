import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

np.random.uniform()

def mc_integral(f, a, b, N):
    '''
    Perform Monte Carlo definite integration of a continuous function
    between interval a and b
    
    f : function of one variable
    a, b : lower and upper bound for integration
    N : sample size
    '''
    y_s = f(np.random.uniform(a, b, N))
    return np.sum(y_s) / (N-1) * (b-a)


def f1(x):
    '''
    a = 1, b=5
    '''
    return x*x

def f2(x):
    '''
    a = 2, b = 3
    '''
    return x**2 + 4*x*np.sin(x)

def f3(x):
    '''
    a = 0, b = 4
    '''
    inside = 15*x**3 + 21*x**2 + 41*x + 3
    return inside**(1/4) * np.exp(-0.5 * x) 



funcs = [f1, f2, f3]
aa = [1, 2, 0]
bb = [5, 3, 4]
titles = [r"$f(x) = x^2$", r"$f(x) = x^2 + 4x sin(x)$", r"$f(x)=\sqrt[4]{15x^3 + 21x^2 + 41x + 3} e^{-0.5x}$"] 

# analytical solution
sol = [41.333, 11.814, 5.767]

# f, ax = plt.subplots(1, 3)
# for i in range(3):
#     ax[i].axhline(sol[i], c='r', label='analytical solution')
#     ax[i].set_title(titles[i])
#     for _ in range(100):
#         integrals = []
#         Ns = range(100, 10500, 500)
#         for N in Ns:
#             integral = mc_integral(funcs[i], aa[i], bb[i], N) 
#             integrals.append(integral)
        
#         ax[i].plot(Ns, integrals, alpha=0.1)
#         ax[i].grid()
#         ax[i].set_xlabel('Number of samples')
#         ax[i].set_ylabel('Integral')
#         ax[i].set_xlim(100, 10000)
#     ax[i].legend()



# Distributions for f2

def plot_distribution(func, a, b, low_x, hi_x):

    f, ax = plt.subplots(3, 3)
    # Number of realizations
    for i, N_realizations in enumerate([50, 100, 1000]):
        i1_all, i2_all, i3_all = [], [], []
        for _ in range(N_realizations):
            Ns = [100, 500, 1000]
            i1 = mc_integral(func, a, b, Ns[0])
            i2 = mc_integral(func, a, b, Ns[1])
            i3 = mc_integral(func, a, b, Ns[2])
            
            i1_all.append(i1)
            i2_all.append(i2)
            i3_all.append(i3)
        
        ax[i][0].hist(i1_all)
        ax[i][0].set_ylabel(f'{N_realizations} realizations')
        ax[i][0].grid()
        ax[i][0].set_xlim(low_x, hi_x)

        ax[i][1].hist(i2_all)
        ax[i][1].grid()
        ax[i][1].set_xlim(low_x, hi_x)

        ax[i][2].hist(i3_all)
        ax[i][2].grid()
        ax[i][2].set_xlim(low_x, hi_x)

        if i == 0:
            ax[i][0].set_title('N = 100')
            ax[i][1].set_title('N = 500')
            ax[i][2].set_title('N = 1000')

    plt.show()

i = 2
# plot_distribution(funcs[i], aa[i], bb[i], 11.75, 12.07)
plot_distribution(funcs[i], aa[i], bb[i], 5, 6.5)


