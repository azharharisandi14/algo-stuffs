import numpy as np
import matplotlib.pyplot as plt

def circle(x0, x1, dx, r):
    """
    r^2 = (x-0.4)^2 + (y+0.4)^2
    r^2 - (x-0.4)^2 = (y+0.4)^2
    sqrt(r^2 - (x-0.4)^2) = y + 0.4
    y = sqrt(r^2 - (x-0.4)^2) - 0.4
    """
    xs = np.arange(x0, x1+dx, dx)
    return xs, np.sqrt(r - (xs-0.4)**2) - 0.4

def numerical_integration(f, t0, tf, dt):
    """
    integrate numerically using trapezoidal method
    
    params
    --------
    f(t):
     parametric equation of a curve 
     (must return x and y for every parameter t)
     
    t0, tf:
     initial and final value for the parameter
     
    dt:
     parameter's spacing (in degree for this particular case)

    
    return
    --------
    area under the curve 
    """
    # discretize based on angle
    t = np.arange(t0, tf+np.deg2rad(dt), np.deg2rad(dt))
    
    # constraint 
    if t[-1] > tf:
        t[-1] = tf
    
    # x_i, f_i 
    x_before, y_before = f(t[:-1])
    
    # x_{i+1}, f_{i+1}
    x_after, y_after = f(t[1:])
    
    # delta x
    dx = abs(x_after - x_before)

    # trapezoid
    return np.sum((abs(y_before) + abs(y_after)) * dx / 2)

def luastrap(xs, ys):
    x_after, x_before = xs[1:], xs[:-1]
    y_after, y_before = ys[1:], ys[:-1]
    dx = abs(x_after - x_before)
    return np.sum((abs(y_before) + abs(y_after))*dx / 2)


# jawaban
x0, x1, dx = 0., 2., 0.1
x, y = circle(x0, x1, dx, 5)
luas = luastrap(x, y)
print('luas area di kuadran 1 : ', luas)


plt.plot(x, y)
plt.ylim(0)
for each_x, each_y in zip(x, y):
    plt.plot([each_x, each_x], [0, each_y], 'k--', alpha=0.2)
# plt.axis('scaled')
plt.show()

    
