import math
import matplotlib.pyplot as plt
import numpy as np

import seaborn as sns

def newton(f,x0, maxiter=100, TOL=1e-6, H=1e-6, MINDF=1e-7):
   def pderfce(f, x,col):
       dx = np.zeros(n)  # vektor samych nul
       dx[col] = H  # na danou pozici
       return (f(x + dx) - f(x - dx)) / (2 * H)
   n=x0.shape[0] # dimenze problemu
   J = np.zeros((n,n)) # sem si ulozim Jacobiovu matici, bude n*x
   x=x0
   fx = f(x)
   for i in range(maxiter):

       # vypocet derivaci f do matice J
        for col in range(n):
            J[:,col] =pderfce(f,x,col)

        if np.fabs(np.linalg.det(J)) < TOL: # kdyz to bude singularni tak skonci
            return  x, fx

        h = np.linalg.solve(J,-fx)
        x=x+h
        fx=f(x)
        if np.linalg.norm(h) < TOL or np.linalg.norm(fx)<TOL:
            return x,fx
   return x, fx



def fce(x):
    f1 = x[0]**2+x[1]**2-1
    f2 = (x[0]/2) ** 2 + (x[1]/0.5) ** 2 - 1
    return np.array((f1,f2))

if __name__=="__main__":
    # vypocet jednoho z korenu
    x0= np.array((0.5,0.5))
    x,fx = newton(fce,x0)
    print(f"Reseni:\t{x}\t{fx}")

    # kresleni heatmapy
    xx = np.arange(-2,2,0.01)
    yy = np.arange(-1,1,0.01)
    mat = np.zeros((len(yy), len(xx)))
    for i, xs in enumerate(xx):
        for j, ys in enumerate(yy):
            x0 = np.array((xs, ys))
            #print(x0)
            x, fx = newton(fce, x0)
            mat[j,i]=x[0]+x[1]

    ax = sns.heatmap(mat)
    plt.show()






