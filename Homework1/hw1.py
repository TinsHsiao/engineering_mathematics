import numpy as np
import matplotlib.pyplot as plt
def f1 ( x ) :
    y = np.exp ( -x ) * np.sin ( 2 * x )
    return y
def f2 ( x ) :
    y = np.exp ( -x ) * np.cos ( 3 * x )
    return y
x = np.linspace ( 0, 2 * np.pi, 100 ) # 於 [0, 2] 產生 100 個點
y1 = f1 ( x )
y2 = f2 ( x )
plt.plot ( x, y1, '-', x, y2, '--' ) # 繪製函數曲線
plt.xlabel ( 'x' )
plt.ylabel ( 'f(x) & g(x)' )
plt.title ( 'Plot of Two Functions' )
plt.text ( 4, -0.2, 'Copyright @ Hsiao' ) # 請加上你的數位簽章
plt.grid()
plt.show ( )