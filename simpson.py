import numpy as np
import  math


def integrace_simpson(f, a, b, maxiter=20, EPS=1e-4):
    h=b-a
    Ih = 0
    for i in range(1,maxiter):
        x=np.arange(a,b+h/2,h/2) # generuj body s polovicnim krokem oproti licho
        fx = f(x)
        h=h/2
        Ih_new = h/3*(fx[0]+4*np.sum(fx[1:-1:2])+2*np.sum(fx[2:-2:2])+fx[-1])
        #print(f"x={x}")
        # print(f"f(x)={x}")
        print(f"{i}:{h}-->{Ih_new}")
        # print("*"*20)
        #print(Ih_new)

        if math.fabs(Ih_new-Ih)< EPS:
            return Ih_new
        Ih = Ih_new
    return Ih_new





if __name__=="__main__":
    fce=lambda x:np.cos(x**2)**2
    a=0
    b=math.pi/2

    I = integrace_simpson(fce, a, b)
