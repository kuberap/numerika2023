import numpy as np
import matplotlib.pyplot as plt


def rhs(c):
    def fce(x,y):
        """
        Funkce pro pravou stranu ODR
        :param x: - představuje čas t
        :param y: - představuje N
        :return:
        """
        return y*(1-c*y)
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

def res_rk2(fce, x0, y0, maximal_x, h=1e-1, maxiter=100_000):
    y = [y0]
    x = [x0]

    while x[-1] <= maximal_x:
        yk=y[-1]
        xk=x[-1]
        substep=h * fce(xk, yk) # udelej krok eulerem
        y.append(yk+h*fce(xk+h/2,yk+substep/2)) # vem pulku y toho kroku a pouzij ho do f
        x.append(xk+h)
        if len(x)>maxiter:
            return x,y
    return x,y






if __name__=="__main__":
    c = 0.01
    f = rhs(c)
    x_euler,y_euler = res_euler(f,x0=0,y0=10,maximal_x=20, h=0.01)
    x_rk2, y_rk2 = res_rk2(f, x0=0, y0=10, maximal_x=20, h=0.01)

    plt.plot(x_euler,y_euler,label=f"Vyvoj ODR Eulerova metoda:{c}")
    plt.plot(x_rk2, y_rk2, label=f"Vyvoj ODR RK2 metoda:{c}")

    plt.grid()
    plt.legend()
    plt.show()