import  numpy as np
import matplotlib.pyplot as plt

n = 5  # rozmer testovaci matice
A = 10*np.random.random((n, n))
w,v = np.linalg.eig(A)
re = [w.real for l in w]
im = [w.imag for l in w]

plt.scatter(x=re, y=im, color="red")
plt.grid()
plt.show()



