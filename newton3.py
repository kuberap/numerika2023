import math
import matplotlib.pyplot as plt
import numpy as np

def newton(f,x0, maxiter=100, TOL=1e-6, H=1e-6, MINDF=1e-7):
    def derffce(f,x):
        return (f(x+H)-f(x-H))/(2*H)
    x=x0
    fx = f(x)
    for i in range(maxiter):
        df = derffce(f,x)
        assert  math.fabs(df)> MINDF, f"Nulová derivace v bodě {x}\t{df}"
        xnew=x-fx/df
        fx = f(xnew)
        print(f"Iterace:{i}-->{xnew}:f(x)={fx}")
        if math.fabs(x-xnew)<TOL or math.fabs(fx)<TOL:
            return xnew, fx
        x=xnew

    return x, fx

if __name__=="__main__":
    N=100
    body = np.random.rand(N)
    print(f"Prumer:{np.mean(body)}")
    fx = lambda x: np.sum((x-body)**2)
    dfx = lambda x: (fx(x+1e-6)-fx(x-1e-6))/(2*1e-6)
    y, f = newton(dfx,1)
    print(f"Reseni:\t{y}\t{f}")

    plt.scatter([ i for i in range(N) ], body)
    plt.hlines(y,0,N)
    plt.grid()
    plt.show()

