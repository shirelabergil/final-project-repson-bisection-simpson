import sympy as sym
import math
from datetime import datetime

print("\n*** BISECTION METHOD ***\n")

def bisection(f, a, b, N, e):
    '''
    Approximate solution of f(x)=0 on interval [a,b] by bisection method.

    Parameters
    ----------
    f : function
    The function for which we are trying to approximate a solution f(x)=0.
    a,b : numbers
    The interval in which to search for a solution. The function returns
    None if f(a)*f(b) >= 0 since a solution is not guaranteed.
    N : (positive) integer
    e : tolerance error
    The number of iterations to implement.

    Returns
    -------
    x_N : number
    The midpoint of the Nth interval computed by the bisection method. The
    initial interval [a_0,b_0] is given by [a,b]. If f(m_n) == 0 for some
    midpoint m_n = (a_n + b_n)/2, then the function returns this solution.
    If all signs of values f(a_n), f(b_n) and f(m_n) are the same at any
    iteration, the bisection method fails and return None.
    '''
    print('\033[1m'+f'\n\nBISECTION METHOD FOR [{a},{b}]\n'+'\033[0m')
    if f(a) * f(b) >= 0:
        print("Bisection method fails.")
        return None
    print(f'Tolerance error : {e}\n')
    a_n = a
    b_n = b
    for n in range(1, N + 1):
        m_n = (a_n + b_n) / 2
        f_m_n = f(m_n)
        print(f'Iteration : {n}, x : {m_n}, f(x): {f_m_n}')
        if f(a_n) * f_m_n < e:
            a_n = a_n
            b_n = m_n
        elif f(b_n) * f_m_n < e:
            a_n = m_n
            b_n = b_n
        elif abs(f_m_n) <= e:
            print("Found exact solution.")
            return m_n
        else:
            print("Bisection method fails.")
            return None
    return (a_n + b_n) / 2


def f(x):
    cos_x = x**2+5*x+6
    return math.cos(cos_x)/(2*float(math.e)**(-1*x))


# Range division
print("Range division : ")
current = -1.5
i = 1
roots_ranges = []
while i <= 35:
    next = current + 0.1
    if f(current)*f(next) < 0 and i < 35:
        print('\033[91m')
        print(f'{i}) x : {current}, f(x) : {f(current)}')
        print(f'{i+1}) x : {next}, f(x) : {f(next)}')
        print('\033[0m')
        roots_ranges.append((current, next))
        i += 2
        current = next+0.1
    else:
        print(f'{i}) x : {current}, f(x) : {f(current)}')
        i += 1
        current = next

if len(roots_ranges) == 0:
    print('\033[0m'+"Roots not found."+'\033[0m')

else:
    roots = []
    for r in roots_ranges:
        roots.append(bisection(f, r[0], r[1], 15, 0.0001))

    print('\n\033[1m'+"The roots :"+'\033[0m')
    now = datetime.now()
    add = '00000' + str(now.day) + str(now.hour) + str(now.minute)
    for i in range(len(roots)):
        print(f'root {i+1} : {str(roots[i]) + add}')

