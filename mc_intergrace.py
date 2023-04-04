import math
import random
import matplotlib.pyplot as plt
import numpy as np
if __name__=="__main__":
    MAXITER = 1000_000
    result = []
    inner_points = 0
    for i in range(1,MAXITER+1):
        p = np.random.rand(3)
        if p @ p <= 1:
            inner_points+=1
        if i % 1000 == 0:
            result.append(6*inner_points/i)

print(result[-1])
plt.plot(result)
plt.axhline(y = math.pi, color = 'r', linestyle = '-')
plt.title("Konvergence k PI")
plt.grid()
plt.show()

