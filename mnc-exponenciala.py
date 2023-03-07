import numpy as np
import matplotlib.pyplot as plt

def generuj_X(flist, t):
    X = np.zeros((len(t), len(flist)))
    for i, fce in enumerate(flist):
        X[:, i] = fce(t)
    return X

t = np.array([0,1,2,3,4,5,6])
N = np.array([2,5,9,15,34,68,130])




f1 = lambda t : np.ones(len(t))
f2 = lambda t :t

flist = [f1,f2]
X = generuj_X(flist, t)

XTX =  X.transpose() @ X
XTty = X.transpose() @ np.log(N) ### pouzivam logaritmus N
alphas = np.linalg.solve(XTX, XTty)
print(f"koeficienty logaritmovaneho modelu> {alphas}") #

a = np.exp(alphas[0]) # prepocet na a s vlnovkou
b = alphas[1] # vem si to b

# kresleni grafu - spocitam si jeho body
t_graf=np.linspace(t[0],t[-1]) # generuj si hodnoty pro graf
y_graf = a*np.exp(b*t_graf) ## pouyita funkce

plt.scatter(x=t, y=N)
plt.plot(t_graf, y_graf, label="prolozeno")
plt.title(f"Data y = {a:.3}*exp({b:.3}*t)")
plt.xlabel("T [den]")
plt.ylabel("N ")
plt.grid()
plt.legend()
plt.show()
