import matplotlib.pyplot as plt
import numpy as np

if __name__=="__main__":

    h = np.array([177,167,192,176,180,182,178,176,177,176,181])
    m = np.array([78,60,85,71,70,71,60,78,84,83,100])

    A = np.ones((len(h),2))
    A[:,0] = h
    print(A)
    AtA = A.transpose() @ A
    Atb = A.transpose() @ m

    koef = np.linalg.solve(AtA, Atb)
    err = np.linalg.norm(A@koef-h)/len(h) # chyba vztazena na pocet prvku
    print(f" Koeficienty {koef}")
    print(f"MSE:{err}")
    x_graf = np.linspace(min(h), max(h), 200)
    y_graf = np.polyval(koef, x_graf)
    plt.plot(x_graf, y_graf, label="Model")
    plt.scatter(x=h,y=m)
    plt.xlabel("vyska h [cm]")
    plt.ylabel("vaha m [kg]")
    plt.grid()
    plt.legend()
    plt.show()
