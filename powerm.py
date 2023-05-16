import  numpy as np
import matplotlib.pyplot as plt



def getmaxlambda(A, maxiter = 100, symetry_eps=1e-6, w_eps=1e-8):
    x = np.random.rand(A.shape[0])  # generuj si nahodne matici - realnych
    w = np.inf # pocatecni lambda
    if np.linalg.norm(A.T-A)>symetry_eps: # tak asi nebude symetricka
        x = x + 1.j*np.random.rand(A.shape[0]) # pricti nahodne imaginarni
    for k in range(maxiter):
        xnew = (A @ x)/(x @ x)
        wnew = (xnew @ x)
        if np.abs(wnew-w) < w_eps:
            return wnew, xnew/np.sqrt(xnew @ xnew), True
        x = xnew
        w = wnew
    return w,xnew/np.sqrt(xnew @ xnew), False # neco to vraci, ale vim, ze bzlo malo iteraci




if __name__=="__main__":
    n = 5 # rozmer testovaci matice
    A = np.random.random((n,n))
    A = A.T @ A
    w,v = np.linalg.eig(A)
    print(f"Vlastni cislo:{w[0]} ")
    print(f"Vlastni vektor:{v[:,0]} ")
    ww,vv, suc = getmaxlambda(A)
    print(f"Moje vlastni cislo: {ww}\t{suc}")
    print(f"Muj vlastni vektor: {vv}\t{suc}")
    print( A @ vv - ww*vv)



