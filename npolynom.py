import cmath
import math

import numpy as np
import random
#
# def newton(f,x0, maxiter=100, TOL=1e-6, H=1e-6, MINDF=1e-7):
#     def derffce(f,x):
#         return (f(x+H)-f(x-H))/(2*H)
#     x=x0
#     fx = f(x)
#     for i in range(maxiter):
#         df = derffce(f,x)
#         assert  math.fabs(df)> MINDF, f"Nulová derivace v bodě {x}\t{df}"
#         xnew=x-fx/df
#         fx = f(xnew)
#         print(f"Iterace:{i}-->{xnew}:f(x)={fx}")
#         if math.fabs(x-xnew)<TOL or math.fabs(fx)<TOL:
#             return xnew, fx
#         x=xnew
#
#     return x, fx

def pbounds(p):
    assert len(p)>1," Polynom musi byt stupne nejmene 1"
    R1 = (1+max(np.fabs(p[:-1]))/np.fabs(p[-1]))**(-1)
    R2 = (1+max(np.fabs(p[1:]))/np.fabs(p[0]))
    return R1,R2

def get_x0(R1,R2, cplx=True):
    R = random.uniform(R1,R2)
    if cplx:
        phi = random.uniform(0,2*math.pi)
        return complex(R*math.cos(phi), R*math.sin(phi))
    else:
        if random.random()>0.5:
            return R
        else:
            return -R





if __name__=="__main__":
    p = [4,-6,9,-12]
    x0= get_x0(*pbounds(p),False)
    print(x0)
