import random
import numpy as np
import math
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

def mc_direct_sampling(f, fmax, a, b, N):
    '''
    perform direct sampling using uniform RNG
    f : function of one variable
    fmax : maximum value for f in a given interval
    a, b : lower and upper bound of integration
    N : Sample size
    '''
    hit = {'x': [], 'y': []}
    miss = {'x': [], 'y': []}
    for _ in range(N):
        x = random.uniform(a, b)
        y = random.uniform(0, fmax)
        if y < f(x):
            hit['x'].append(x)
            hit['y'].append(y)
        else:
            miss['x'].append(x)
            miss['y'].append(y)
            
    return hit, miss, len(hit['x'])/N * (b-a) * fmax


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
maxs = [25, 13, 2]
titles = [r"$f(x) = x^2$", r"$f(x) = x^2 + 4x sin(x)$", r"$f(x)=\sqrt[4]{15x^3 + 21x^2 + 41x + 3} e^{-0.5x}$"] 
Ns = [100, 300, 600, 1000]


# # plot hit and miss points for each N
# f, ax = plt.subplots(4, 3, figsize=(20, 25))
# for row, N in enumerate(Ns):
#     for i, f in enumerate(funcs):
#         x = np.linspace(aa[i], bb[i])
#         hit, miss, integral = mc_direct_sampling(f, maxs[i], aa[i], bb[i], N) 
#         integral2 = mc_integral(f, aa[i], bb[i], N)
#         ax[row][i].plot(x, f(x), c='k', linewidth=2)
#         ax[row][i].scatter(hit['x'], hit['y'], c='g')
#         ax[row][i].scatter(miss['x'], miss['y'], c='r')
#         if row == 0:
#             ax[row][i].set_title(titles[i])

#         if i == 0:
#             ax[row][i].set_ylabel(f'N = {N}')

#         ax[row][i].grid()

#         props = dict(boxstyle='round', facecolor='white', alpha=0.9)
#         ax[row][i].text(bb[i] - 0.5*(bb[i]-aa[i]), 0, f"integral = {integral:.3f}", 
#                         bbox=props, fontsize=14)

        
# # Multiple realizations example for f1
# plt.figure()
# for _ in range(50):
#     integrals = []
#     # new set of N
#     Ns = range(100, 10500, 500)
#     for N in Ns:
#         _, _, integral = mc_direct_sampling(f1, maxs[0], aa[0], bb[0], N)
#         integrals.append(integral)
#     plt.plot(Ns, integrals, alpha=0.2)
# plt.axhline(41.333, c='r', label='analytical solution') # analytical solution
# plt.legend()
# plt.grid()
# plt.xlim(100, 10000)
# plt.xlabel('N (Sample Size)')
# plt.ylabel('Integral')


# distributions
def plot_distribution(fun, max, a, b, x_lo, x_hi):
    f, ax = plt.subplots(3, 3)
    # Number of realizations
    for i, N_realizations in enumerate([50, 100, 1000]):
        i1_all, i2_all, i3_all = [], [], []
        for _ in range(N_realizations):
            Ns = [100, 500, 1000]
            _, _, i1 = mc_direct_sampling(fun, max, a, b, 100)
            _, _, i2 = mc_direct_sampling(fun, max, a, b, 500)
            _, _, i3 = mc_direct_sampling(fun, max, a, b, 1000)
            i1_all.append(i1)
            i2_all.append(i2)
            i3_all.append(i3)
        
        ax[i][0].hist(i1_all)
        ax[i][0].set_ylabel(f'{N_realizations} realizations')
        ax[i][0].grid()
        ax[i][0].set_xlim(x_lo, x_hi)

        ax[i][1].hist(i2_all)
        ax[i][1].grid()
        ax[i][1].set_xlim(x_lo, x_hi)

        ax[i][2].hist(i3_all)
        ax[i][2].grid()
        ax[i][2].set_xlim(x_lo, x_hi)

        if i == 0:
            ax[i][0].set_title('N = 100')
            ax[i][1].set_title('N = 500')
            ax[i][2].set_title('N = 1000')

    plt.show()

i = 2
plot_distribution(funcs[i], maxs[i], aa[i], bb[i], 4, 7.4)










