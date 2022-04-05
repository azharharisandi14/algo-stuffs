import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return (x**2 + y) * np.sin(x**2 * y)

def rk4(f, x0, y0, xt, h):
    '''
    x0 = initial x
    y0 = initial y
    xt = final x
    h = stepsize
    '''
    
    # initial condition
    y = [y0]
    x = [x0]

    # loop until desired x
    for i in range(int((xt-x0)/h)):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h/2, y[i] + h*k1/2)
        k3 = f(x[i] + h/2, y[i] + h*k2/2)
        k4 = f(x[i] + h, y[i] + h*k3)
        y.append(y[i] + h/6*(k1 + 2*k2 + 2*k3 + k4))
        x.append(x[i] + h)
        
    return x,y


# poin (i)
x_initial, y_initial = 0, 5
x_final = 2
h = 0.2
x, hasil_i = rk4(f, x_initial, y_initial, x_final, h)
print("solusi dengan stepsize 0.2 : ", x, hasil_i)
plt.figure()
plt.plot(x, hasil_i, label='h=0.2')
plt.grid()
plt.legend()
plt.xlabel('x')
plt.ylabel('y')

# poin (ii)
hs = [0.01, 0.1]
col = ['r', 'b']
plt.figure()
for i, h in enumerate(hs):
    x, y = rk4(f, x_initial, y_initial, x_final, h)
    plt.plot(x, y, '.-', label=f'h={h}', c=col[i])
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
