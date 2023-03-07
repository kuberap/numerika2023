import numpy as np
import matplotlib.pyplot as plt

t = np.array([0,10,41,69,100,130,161,181,191,222,253,283,314,344])
d = np.array([655,657,676,705,740,772,796,801,799,782,752,718,685,661])

plt.scatter(x=t, y=d)
plt.title("Delka svetla")
plt.xlabel("T [den]")
plt.ylabel("D [min]")
plt.grid()
plt.show()
