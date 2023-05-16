import  numpy as np
import matplotlib.pyplot as plt

n = 5  # rozmer testovaci matice
A = 100*np.random.random((n, n))
w,v = np.linalg.eig(A)
print(w)
re = [w.real for l in w]
im = [w.imag for l in w]

centres = [ A[i,i] for i in range(n)]
radius = [ np.sum(np.abs(A[i,:]))-A[i,i] for i in range(n)]

fig, ax = plt.subplots()
plt.scatter(x=re, y=im, color="red")
for c,r in zip(centres, radius):

    ax.add_patch(plt.Circle((c,0), radius=r, color="pink"))
plt.scatter(x=re, y=im, color="red")
#plt.scatter(x=centres, y=np.zeros(n), color="blue")

plt.grid()
plt.show()



