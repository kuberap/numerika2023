import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
print(df.columns)
df.dropna(inplace=True)

X=df[['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax',
       'ptratio', 'b', 'lstat']]
y=df[['medv']]
# normalizace dat
X=X-X.min()
X=X/X.max()
print(X.head(10))

XTX = X.transpose() @ X
XTty = X.transpose() @ y

alphas = np.linalg.solve(XTX, XTty)
print(alphas.flatten())
print(['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax',
       'ptratio', 'b', 'lstat'])





