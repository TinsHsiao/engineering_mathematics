import numpy as np 
import matplotlib.pyplot as plt

def f1(x) :
    y = -8/5*np.exp(-x)-1/15*np.exp(-6*x)+5/3
    return y

def f2(x) :
    y = -4/5*np.exp(-x)+2/15*np.exp(-6*x)+2/3
    return y
x = np.linspace( 0, 2*np.pi, 500 )
y1 = f1(x)
y2 = f2(x)
plt.plot ( x, y1, '-', x, y2, '--' )
plt.xlabel( 'x' )
plt.ylabel( 'f(x)' )
plt.title( "Plot of the Function f(x)")
plt.text( 1, -0.3, 'Copyright@ Hsiao')
plt.show()

#10-1 y = np.cos(x) +np.sin(x)+x-1
#10-2 y = -np.cos(x)+np.sin(x)+x-1
#11-1 y = -8/5*np.exp(-x)-1/15*np.exp(-6*x)+5/3
#11-2 y = -4/5*np.exp(-x)+2/15*np.exp(-6*x)+2/3