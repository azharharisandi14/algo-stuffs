def f(x, y):
    return (1+y**2)/2

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
        k1 = f(i, y[i])
        k2 = f(i + h/2, y[i] + h*k1/2)
        k3 = f(i + h/2, y[i] + h*k2/2)
        k4 = f(i + h, y[i] + h*k3)
        y.append(y[i] + h/6*(k1 + 2*k2 + 2*k3 + k4))
        x.append(x[i] + h)
        
    return x,y


def temp(t, teta):
    return -2.2067*1e-12 * (teta**4 - 8.1*1e9)


import matplotlib.pyplot as plt

# final time
final_time = 10000

# plotting
f, ax = plt.subplots(1, 2)
hs = [10, 30, 60, 120, 240, 480]
ts = []
for h in hs:
    x, y = rk4(temp, 0, 1200, final_time, h)
    print(f'stepsize {h} - took {len(x)} iteration')
    print(f'final temperature : {y[-1]}')
    print(' ')
    ax[0].plot(x, y, '.-', label=f'h={h}')
    ts.append(y[-1])
    
    
ax[0].set_xlabel('Time (s)')
ax[0].set_ylabel('Temperature (K)')
ax[0].grid()
ax[0].legend()

ax[1].plot(hs, ts, '.-', c='k')
ax[1].set_xlabel('h')
ax[1].set_ylabel(f'Temperature  at {final_time} s (K)')
ax[1].grid()

plt.show()

    
    
