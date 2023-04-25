import cmath
import math
import warnings

import numpy as np
import random
#
def newton(p,x0, maxiter=100, TOL=1e-8, MINDF=1e-7):
    n = len(p)-1
    dp = [ (n-i)*v for i,v in enumerate(p[:-1])]
    f = lambda x: np.polyval(p,x)
    derffce = lambda x: np.polyval(dp,x)
    x=x0
    fx = f(x)
    for i in range(maxiter):
        df = derffce(x)
        assert  abs(df)> MINDF, f"Nulová derivace v bodě {x}\t{df}"
        xnew=x-fx/df
        fx = f(xnew)
        # print(f"Iterace:{i}-->{xnew}:f(x)={fx}")
        if abs(x-xnew)<TOL or abs(fx)<TOL:
            return xnew, fx
        x=xnew

    return x, fx

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

def poly_solve(p, MAX_ATTEPMTS=10, NEWTON_MAXITER=100, TOL=1e-8, MINDF=1e-7, CTOL=1e-8):
    roots = []
    n = len(p) -1 # kolik budu hledat korenu
    for attempt in range(MAX_ATTEPMTS):
        x0 = get_x0(*pbounds(p))
        root, px = newton(p, x0, NEWTON_MAXITER,TOL, MINDF)
        if abs(px) < TOL: # kdyz je to skoro nula - koren to naslo
            # kdyz je koren realny
            print(root)
            if abs(root.imag)<CTOL: # tedy komplexni je skoro nula
                roots.append(root)
                p = np.polydiv(p, [1, -root.real])[0]  # kdyz to ten koren naslo, tak del p/(1*x-koren)
                # print(f"REAL")
                # print(f"{attempt}-->{root}")
                # print(f"{attempt}p-->{p}")
            else: #koren je komplexni
                roots.append(root)
                roots.append(root.conjugate())
                dp = np.polymul([1,-root],[1, -root.conjugate()])
                p = np.polydiv(p, dp)[0]
                # print(f"COMPLEX")
                # print(f"{attempt}-->{root}===={root.conjugate()}")
                # print(f"{attempt}dp-->{dp}")
                # print(f"{attempt}p-->{dp}")
            if len(roots) == n: # kdyz jsem nasel n korenu
                return roots

    return roots


if __name__=="__main__":
    p = [4,-6,9,-12]
    roots = poly_solve(p)
    print(roots)

