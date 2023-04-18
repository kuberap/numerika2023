import math

import matplotlib.pyplot as plt

def newton(f,x0, maxiter=100, TOL=1e-4, H=1e-6):
    def derffce(f,x):
        return (f(x+H)-f(x-H))/(2*H)
    x=x0
    fx = f(x)
    for i in range(maxiter):
        df = derffce(f,x)
        assert  math.fabs(df)>1e-6, f"Nulová derivace v bodě {x}\t{df}"
        xnew=x-fx/df
        fx = f(xnew)
        print(f"Iterace:{i}-->{xnew}:f(x)={fx}")
        if math.fabs(x-xnew)<TOL or math.fabs(fx)<TOL:
            return xnew, fx
        x=xnew

    return x, fx

if __name__=="__main__":
    fx = lambda x: x+math.log(x)
    x, f = newton(fx,0.7)

    print(f"Reseni:\t{x}\t{f}")






