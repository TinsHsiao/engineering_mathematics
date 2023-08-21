import matplotlib.pyplot as plt 
import numpy as np



# a
X = np.arange(-5,5,0.5)
Y = np.arange(-5,5,0.5)

x,y = np.meshgrid( X,Y )

dy = np.sin(x)*np.cos(y)
dx = 1

norm = np.sqrt( dx*dx + dy*dy ) #改這邊
dy = dy/norm
dx = dx/norm


"""
# b
X = np.linspace(0,2*np.pi,200)
Y = np.linspace(0,2*np.pi,200)

x,y = np.meshgrid( X,Y )

z = (x*y) + (2*y + y*np.exp(y)-np.exp(y)) + (np.exp(x))
"""
"""
# c
X = np.linspace(-2,2,200)
Y = np.linspace(-2,2,200)

x,y = np.meshgrid( X,Y )

z = y + 2 np.log10(np.exp(np.absolute(y))) + np.log10(np.exp(np.absolute(np.sin(x))))
"""
"""
# d
X = np.linspace(-2* np.pi,2* np.pi,200)
Y = np.linspace(-2* np.pi,2* np.pi,200)

x,y = np.meshgrid( X,Y )

z = y*np.cos(x) + x*np.sin(y) - y**2/2
"""

plt.figure(1)
q = plt.quiver(x, y, dx, dy)

plt.xlabel( 'x' )
plt.ylabel( 'y' )
plt.title( 'Direction Field' )
plt.grid()
plt.text( 2, -7,'Copyright @ tzujou')

plt.show()