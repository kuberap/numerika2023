import numpy as np
import matplotlib.pyplot as plt

def generuj_X(flist, t):
    X = np.zeros((len(t), len(flist)))
    for i, fce in enumerate(flist):
        X[:, i] = fce(t)
    return X

t = np.array([0,10,41,69,100,130,161,181,191,222,253,283,314,344])
d = np.array([655,657,676,705,740,772,796,801,799,782,752,718,685,661])

# lehce genialni obrat pro automatizaci mnc
"""
Definuji si funkce a pak je dam do seznamu.
Na yaklade funkci v seznamu sestavim matici X
"""
f1 = lambda t : np.ones(len(t))
f2 = lambda t : np.cos(2*3.14/365.25*t)
f3 = lambda t : np.sin(2*3.14/365.25*t)
flist = [f1,f2,f3]
X = generuj_X(flist, t)

XTX =  X.transpose() @ X
XTty = X.transpose() @ d
alphas = np.linalg.solve(XTX, XTty)
print(f"koeficienty {alphas}")
# urci si predikci pro graf - udelam si delsi vektor a overim periodicitu
t_graf = np.arange(t[0],2*t[-1])
Xgraf = generuj_X(flist, t_graf)
y_predikce = Xgraf @ alphas


plt.scatter(x=t, y=d)
plt.plot(t_graf[:344],y_predikce[0:344], color="red", label="prolozeni")
plt.plot(t_graf[344:],y_predikce[344:], color="green", label="predikce")
plt.title("Delka svetla")
plt.xlabel("T [den]")
plt.ylabel("D [min]")
plt.grid()
plt.show()
