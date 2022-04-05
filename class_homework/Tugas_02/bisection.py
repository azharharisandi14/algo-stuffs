def bisection(fun, a, b, epsilon=0.001):
    """
    function for root finding using bisection method,
    this function iteratively find the midpoint between
    given a and b and stops when fun(m) < epsilon.

    arguments
    ----------
    fun:
        single-variable function
    a:
        lower bound for the search interval
    b:
        upper bound for the search interval
    epsilon:
        small value, threshold for accuracy (default 0.001)


    return
    -----------
    m:
        chosen midpoint where fun(m) < epsilon
    string:
        'choose another interval' when fun(a) and fun(b)
        both have the same sign
    
    """

    # check whether fun(a) and fun(b) have the same sign
    if fun(a) * fun(b) > 0:
        return "choose another interval"

    # midpoint
    m = (a+b)/2

    while abs(fun(m)) > epsilon:
        if fun(b) * fun(m) > 0:
            b = m
            m = (a+b)/2
        else:
            a = m
            m = (a+b)/2

    return m


if __name__ == "__main__":

    # test case 1
    def f(x): return x**2 - 3*x - 2

    # test case 2
    def f2(x): return x**3 + x**2 - 3*x - 2

        
