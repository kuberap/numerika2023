import numpy as np
import matplotlib.pyplot as plt


def rhs(N0,c):
    def fce(x,y):
        """
        Funkce pro pravou stranu ODR
        :param x: - představuje čas t
        :param y: - představuje N
        :return:
        """
        return N0*(1-c*x)
    return fce

def res_euler(fce, x0, y0, maximal_x, h=1e-1, maxiter=100_000):
    y = [y0]
    x = [x0]

    while x[-1] <= maximal_x:
        yk=y[-1]
        xk=x[-1]
        y.append(yk+h*fce(xk,yk))
        x.append(xk+h)
        if len(x)>maxiter:
            return x,y
    return x,y





if __name__=="__main__":
    f = rhs(1000,0.05)
    print(f(1,1))
    x,y = res_euler(f,x0=0,y0=1000,maximal_x=100)

    plt.plot(x,y,label="Vyvoj ODR")
    plt.grid()
    plt.legend()
    plt.show()