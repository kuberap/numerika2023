import gauss
import numpy as np
import math

def fce(a):
    phi = lambda x: np.exp(a*x)*np.cos(x)
    return gauss.integrace_gauss(phi,0, math.pi*3/2) # integruj na danem intervalu

def bisekce(fx, alpha, beta, maxiter=100, TOL=1e-5):
    falpha = fx(alpha)
    fbeta = fx(beta)
    for i in range(maxiter):
        gama = (alpha+beta)/2
        fgama = fx(gama)
        if math.fabs(fgama)<TOL:
            return gama, fgama # koren jsem nasel
        elif fgama*falpha<0: # koren je mezi alpha a gama
            beta = gama
            fbeta = fgama
        else: # koren je mezi gama a beta
            alpha = gama
            falpa = fgama
    return gama, fgama


if __name__=="__main__":
    alpha = -1
    beta = 0
    a, fa = bisekce(fce, -1,0)
    print(f"Hodnota a:{a} hodnota integralu:{fa}")
