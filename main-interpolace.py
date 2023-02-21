import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

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


if __name__ == "__main__":
    x = np.array([1,2,3,4,5,6])
    y = np.array([-1,1,2,-1,-2,1])
    # ziskani koeficeintu
    a = naive_interp(x,y)
    print(f"Koeficienty:{a}")

    x_graf = np.linspace(min(x), max(x),200)
    y_graf = np.polyval(a,x_graf)

    plt.plot(x_graf, y_graf,label= "nalezeny polynom")
    plt.scatter(x,y,label="body vstupu", color = "red")
    plt.grid()
    plt.legend()
    plt.show()

