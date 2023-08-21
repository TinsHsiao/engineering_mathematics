import numpy as np 
import matplotlib.pyplot as plt

def f(x) :
    y = np.cos(2*x) + 1/4 *x*np.sin(2*x)
    return y
    
x = np.linspace( 0, 4*np.pi, 500 )
y = f(x)
plt.plot(x,y)
plt.xlabel( 'x' )
plt.ylabel( 'f(x)' )
plt.title( "Plot of the Function f(x)")
plt.text( 1, 0, 'Copyright@ Hsiao')
plt.show()

#1 y = np.exp(-x)*(2*np.cos(3*x)+(1/3)*np.sin(3*x))
#2 y = np.exp( -x ) *  ( np.cos(3*x)+(1/3) *np.sin(3*x) )
#3 y = np.exp(-x) + np.exp(x) * (np.cos(x) +np.sin(x))
#4 y = np.exp(-4*x) + np.exp(4*x) + (-2/3)*x*np.exp(-4*x)
#5 y = np.cos(2*x) + 1/4 *x*np.sin(2*x)
#6 y = np.cos(x)-np.sin(x)+(1/4*np.cos(x)+1/12*cos(3x))+(3/4*np.sin(x)+1/12*np.sin(3*x))*sinx
#7 y = x + x*x + x*np.exp(x)
#8-1 y = np.exp(-10*x)*(0.0015*np.cos(30*x)+0.0069*np.sin(30*x))-0.0015*np.cos(60*x)-0.0032*np.sin(60*x)
#8-2 y=-10*np.exp(-10*x)*(0.0015*np.cos(30*x)+0.0069*np.sin(30*x))\
#        +np.exp(-10*x)*(-0.045*np.sin(30*x)+0.207*np.cos(30*x))+0.09*np.sin(60*x)\
#            -0.192*np.cos(60*x)
#9-1 y = 50*np.cos(10*np.sqrt(10)*x)
#9-2 y = 500*np.sqrt(10)*np.sin(10*np.sqrt(10)*x)