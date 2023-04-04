import gauss
import numpy as np

if __name__=="__main__":
    fx = lambda x: x * np.exp(-x)
    fsubst = lambda t: fx(1/t)/(-t**2)

    for a in [10,100,1000,10000]:
        I1 = gauss.integrace_gauss(fx,0,a)
        I2 = gauss.integrace_gauss(fsubst,1/a,0)
        print(f"{a}>>>Odhad:{I1} Chyba:{I2}")

