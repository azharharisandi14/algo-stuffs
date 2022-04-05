import numpy as np
import matplotlib.pyplot as plt

def circle(teta, r=6):
    """
    parameterized the curve (circle) based on angle
    angle convention : 0 from north (yaxis), 
    and increasing clockwise

    c(t) = (x(t), y(t))
    x(t) = r*sin(t)
    y(t) = r*cos(t)
    
    params
    --------- 
    teta:
     angle/azimuth from north (radian)
    r:
     radius of the circle (default=6)
    
    return
    ---------
     x, y : x and y coordinate of a point in a circle of radius r
    """
    x = r*np.sin(teta)
    y = r*np.cos(teta)
    return x, y


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



if __name__ == "__main__":

    t0, tf = 0, 3/2*np.pi
    dt = 15 # in degree

    # discretized teta
    teta_disc = np.arange(t0, tf+np.deg2rad(dt), np.deg2rad(dt))

    # pseudo-continuous curve
    teta = np.linspace(0, 3*np.pi/2, 100)
    x, y = circle(teta)

    plt.plot(x, y)
    plt.scatter(*circle(teta_disc))
    plt.axhline(0, c='k')
    plt.axvline(0, c='k')
    plt.axis('scaled')
    plt.show()


    # compare to analytical solution
    analytical_solution = 3/4 * np.pi * 6**2
    
    dts = [0.1, 1, 5, 10, 15] # set of intervals
    plt.axhline(analytical_solution, label='analytical solution',c='r')
    plt.plot(dts,
             [numerical_integration(circle, 0, 3*np.pi/2, x) for x in dts],
             '.-', c='k')
    plt.grid()
    plt.xlabel('dt')
    plt.ylabel('Area')
    plt.legend()
    plt.show()
