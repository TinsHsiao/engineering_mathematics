import matplotlib.pyplot as plt 
import numpy as np


x = np.linspace(0,4*np.pi ,200) # d
#x = np.linspace(0, 4*np.pi ,100) # c
#x = np.linspace(0,2*np.pi ,200) # b
#x = np.linspace(3,-3,200) # a

y = np.tan(x)-x-1 # d
#y = np.cos(x) * x + np.cos(x) # c
#y = np.sin((1/2) * (x**2) + np.pi/2 ) # b
#y = np.exp((-1/2)*(x**2)) # a

plt.figure(1)
plt.plot(x, y)
plt.xlabel( 'x' )
plt.ylabel( 'y' )
plt.title( 'f(x) = tan(x) - x -1' )#sin(x*x/2 + pi/2)
plt.text( -0.1, 0 ,'Copyright @ tzujou')