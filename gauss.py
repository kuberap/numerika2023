import numpy as np
import  math


def integrace_gauss(f, a, b, maxiter=20, EPS=1e-6, w=np.array([5/9, 8/9,5/9]), t = np.array([-math.sqrt(3/5), 0, math.sqrt(3/5)]) ):
    def gauss_dilci_interval(f,a,b, w, t):
        tt = (a+b)/2 +t*(b-a)/2 # transformuj si uzle na dilci subinterval
        return (b-a)/2*(w @ f(tt)) # skalarni soucin suma (w_i f(tt_i))

    h=b-a
    Ih_new=0
    for i in range(1,maxiter):
        x=np.arange(a,b+h/2,h) # uzlove body dilcich intervalu
        print(f"Deleni:{x}")
        Ih = 0
        for j in range(len(x)-1):
            Ih+=gauss_dilci_interval(f,x[j],x[j+1],w,t) # spocti integral pres dilci intervaly
        print(f"Iterace:{i}-->{Ih}")
        print("-"*40)
        h = h / 2  # rozpul krok
        if i > 1 and math.fabs(Ih_new-Ih)<EPS:
            Ih_new=Ih
            break
        Ih_new=Ih
    return Ih_new





if __name__=="__main__":
    fce=lambda x:np.cos(x**2)**2
    a=0
    b=math.pi/2
    I = integrace_gauss(fce,a,b)
    print(I)
