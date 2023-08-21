import math
import numpy as np
import matplotlib.pyplot as plt

def f1 ( x ) :
    y = np.sin( x )
    return y 
def f2 ( x ) :
    y = x - np.power ( x, 3 ) / math.factorial(3) \
        + np.power ( x, 5 ) / math.factorial(5) \
        - np.power ( x, 7 ) / math.factorial(7)
    return y
x = np.linspace ( - np.pi, np.pi, 100 ) # 於 [0, 2] 產生 100 個點
y1 = f1 ( x )
y2 = f2 ( x )
plt.plot ( x, y1, '-', x, y2, '--' ) # 繪製函數曲線
plt.xlabel ( 'x' )
plt.ylabel ( 'f(x) & g(x)' )
plt.title ( 'Plot of Two Functions' )
plt.text ( 4, -0.2, 'Copyright @ tzujou' ) # 請加上你的數位簽章
plt.grid()
plt.show ( )