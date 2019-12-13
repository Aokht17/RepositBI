import math
import numpy as np
import matplotlib.pyplot as plt
t = [i for i in np.arange(0, math.pi*2)]
t = list(t)
x = [16*(math.sin(i))**3 for i in t]
y = [13*math.cos(j)-5*math.cos(2*j) - 2*math.cos(3*j) - math.cos(4*j) for j in t]

plt.title('broken heart')
# ok, It was supposed to be a beautiful parametric heart, but something has simply got wrong
# I'll just leave it here
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.plot(x, y, color='red')
