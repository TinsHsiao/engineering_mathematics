import numpy as np
import matplotlib.pyplot as plt
def f ( x ) :
    y = np.exp(-x)*np.sin(2*x)
    return y

x = np.linspace( 0, 2*np.pi, 100 )
y = f ( x )
plt.plot( x, y )
plt.xlabel( 'x' )
plt.ylabel( 'f( x )' )
plt.title( 'Plot of the Function f(x) = exp(-x)*sin(2x)')
plt.text( 4, -0.1, 'Copyroght@ Hsiao' )
plt.show()