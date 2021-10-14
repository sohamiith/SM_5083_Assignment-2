import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-8,10,200)

# first line
plt.plot(x, y, '-r', label='5X-12Y=0')
y = (((5/12)*x)+0)

#second line
plt.plot(x, y, '-g', label='5X+12Y+60=0')
y = (((-5/12)*x)+(-5))

#third line
plt.plot(x, y, '-b', label='12X+5Y-60=0')
y = (((-12/5)*x)+(12))

plt.title('Graph of triangle created by three line')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.grid()
plt.plot(2.536, -2.515, 'ro')
plt.show()