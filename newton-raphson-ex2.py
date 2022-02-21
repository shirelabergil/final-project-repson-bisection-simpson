# importing libraries
import math
import numpy as np
import pandas as pd
import sympy as sym
from datetime import datetime


def newtonRaphson(x0, e, N, f, df, low, up):
    print(f'\nNewton Raphson for : [{low},{up}] , Tolerable error : {e}\n')
    step = 1
    condition = True
    while x0 >= low and x0 <= up:
        if df.subs(x, x0) == 0.0:
            print('Divide by zero error!')
            break
        x1 = x0 - f.subs(x, x0) / df.subs(x, x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f.subs(x, x1)))
        x0 = x1
        step = step + 1
        if step > N:
            print("root not found.")
            return None, False
        condition = abs(f.subs(x, x1)) < e
        if condition:
            print("root found.")
            return x1, True
    print("root not found.")
    return None, False


# Starting Newton Raphson Method
print("\n*** NEWTON RAPHSON METHOD ***\n")
x = sym.Symbol('x')
cos_x = x ** 2 + 5 * x + 6
f = sym.cos(cos_x) / (2 * float(math.e) ** (-1 * x))
derivative_f = f.diff(x)

a = -1.5
b = 2

roots = []
while a != b:
    root, bool = newtonRaphson((a+a+0.5)/2, 0.0001, 10, f,derivative_f, a, a + 0.5)
    if bool:
        roots.append(root)
    a += 0.5

now = datetime.now()
add = '00000' + str(now.day) + str(now.hour) + str(now.minute)

if len(roots) != 0:
    print("\n\nThe roots : ")
    for i in range(len(roots)):
        print(f'root {i+1} : {str(roots[i]) + add}')
else:
    print("roots not found.")