import math

import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt


"""
Vylepšení interpolace pomocí kořenů čeb. polynomu.
"""

def naive_interp(x,y):
    assert len(x)==len(y), "Vstupy maji rozdilnou velikost"
    n=len(x)
    A=np.ones((n, n)) # matice samych jednicek
    tmp = np.ones(n) # vektor jednicek
    # generovani matice
    for i in range(len(x),0,-1):
        A[:,i-1] = tmp
        tmp=tmp*x
    return la.solve(A,y) # vrat vzsledek reseni soustavy rovnic

def lagrange_interp(x,y,xg):
    assert len(x) == len(y), "Vstupy maji rozdilnou velikost"
    n = len(x) # pocet vstupnich bodu
    pocet_bodu = len(xg) # pocet bodu pro ktere bude polynom vyhodnocen
    yg = np.zeros(pocet_bodu) # sem jsou ukladany spoctene body yg = Ln(xg)
    for k in range(pocet_bodu):
        for i in range(n):
            produkt = 1 # slouzi pro ulozeni soucinu
            for j in range(n):
                if j!=i:
                    produkt*=(xg[k]-x[j])/(x[i]-x[j]) # delej soucin
            yg[k]+=y[i]*produkt # delej sumaci
    return yg

def funkce(x):
    return  1/(1+5*x*x) #20*np.sin(2*x)

def vrat_koreny(a,b,n):
    x = np.cos(np.array([(2.0*i+1)/n*math.pi/2.0 for i in range(n)]))
    return 0.5*(b-a)*x+0.5*(a+b)

if __name__ == "__main__":
    x = np.linspace(-10,10,9)#np.array([1,2,3,4,5,6])
    y = funkce(x)  #np.array([-1,1,2,-1,-2,1])
    # ziskani koeficeintu
    a = naive_interp(x,y)
    print(f"Koeficienty:{a}")

    x_graf = np.linspace(min(x), max(x),200)
    y_graf = np.polyval(a,x_graf)

   # y_graf_lagrange = lagrange_interp(x,y,x_graf)
    y_graf_realita = funkce(x_graf)

    # ---------------PRIDANO CHEBy-----------------------
    x_cheby = vrat_koreny(-10,10,9)
    print(f"Uzly cheby:{x_cheby}")
    y_cheby = funkce(x_cheby)
    a_cheby = naive_interp(x_cheby,y_cheby)
    y_graf_cheby = np.polyval(a_cheby, x_graf)
    plt.plot(x_graf, y_graf_cheby, label="Cheby. uzly")
    plt.scatter(x_cheby, y_cheby, label="body vstupu cheby", color="black")
    # -------------- KONEC CHEBY-----------------------
    plt.plot(x_graf, y_graf,label= "nalezeny polynom")
  #  plt.plot(x_graf, y_graf_lagrange, label="Lagrangeuv interpolacni polynom")
    plt.scatter(x,y,label="body vstupu", color = "red")
    plt.plot(x_graf, y_graf_realita, color="green", label="realita")
    plt.grid()
    plt.legend()
    plt.show()

