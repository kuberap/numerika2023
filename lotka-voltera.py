import numpy as np
import matplotlib.pyplot as plt



def rhs(alpha,beta,gama, delta):
    def fce(x,y):
        """
        Prava strana pro Lotka-Voltera model
        :param x: predstavuje cas t
        :param y: predstavuje vektor [korist, dravec]
        :return: vektor [korist, dravec]
        """
        return np.array((alpha*y[0]-beta*y[0]*y[1],delta*y[0]*y[1]-gama*y[1]))
    return fce



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
    alpha = 1
    beta = 0.1
    gama = 0.7
    delta = 0.1

    f = rhs(alpha, beta, gama, delta)

    x_rk2, y_rk2 = res_rk2(f, x0=0, y0=np.array([10,10]), maximal_x=20, h=0.01)

    korist = [item[0] for item in y_rk2]
    dravec = [item[1] for item in y_rk2]

    plt.plot(x_rk2, korist, label=f"Vyvoj Korist")
    plt.plot(x_rk2, dravec, label=f"Vyvoj Dravec")

    plt.grid()
    plt.legend()
    plt.show()

    plt.plot(korist, dravec)
    plt.title("Fazovy diagram")
    plt.xlabel("Korist")
    plt.ylabel("Dravec")
    plt.show()
    plt.grid()