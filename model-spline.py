import numpy as np
import matplotlib.pyplot as plt


def proloz_spline(x,y, xgraf):
    def sestav_matici(h,y):
        k = len(x) - 2  # rozmery matice
        A = np.zeros((k, k))  # udelej si prazdnou matici
        for i in range(k):
            A[i, i] = (h[i] + h[i + 1]) / 3
        for i in range(k - 1):
            A[i, i + 1] = h[i + 1] / 6  # druha diagonala - nad hlavni
            A[i + 1, i] = h[i + 1] / 6  # treti diagonala - pod hlavni
        return A

    h=np.array([ x[i+1]-x[i] for i in range(len(x)-1)])
    Amatice = sestav_matici(h,y)
    # sestaveni prave strany
    g= np.array([-(y[i]-y[i-1])/h[i-1]+(y[i+1]-y[i])/h[i] for i in range(1,len(x)-1)]) # pres vsechny vnitrni body
    # udelej si praydne pole
    M=np.zeros(len(x))
    M[1:-1]=np.linalg.solve(Amatice,g) # spocti momenty a vloz je do pole, krajni M jsou 0

    A = np.array([(y[i+1]-y[i])/h[i] + (M[i]-M[i+1])/6*h[i] for i in range(len(x)-1)])
    B = np.array([y[i]-M[i]/6*h[i]**2 for i in range(len(x)-1)])
    ygraf = []
    last_interval = 0
    for xp in xgraf:# pro kazdy bod grafu
        for i in range(last_interval,len(x)-1):
            if x[i]<=xp<=x[i+1]: # jsem v danem segmentu
                last_interval = i
                break # vyskoc
        i=last_interval
        ygraf.append(-M[i]/(6*h[i])*(xp-x[i+1])**3+M[i+1]/(6*h[i])*(xp-x[i])**3+A[i]*(xp-x[i])+B[i])
    return ygraf










if __name__ == "__main__":
    fce = lambda x: 1.0/(1+5*x**2) # funkci co chci interpolovat

    a,b=-5,5 # interval na kterém provadim interpolaci
    N = 31
    x = np.linspace(a,b,N)
    y = fce(x)

    xgraf = np.linspace(a, b, 200)
    # sestaveni
    yspline = proloz_spline(x,y, xgraf)

    ygraf = fce(xgraf)

    plt.plot(xgraf, ygraf,label = "realita")
    plt.plot(xgraf, yspline, label="spline")
    plt.scatter(x,y)
    plt.title("Interpolacni spline")
    plt.grid()
    plt.legend()
    plt.show()






