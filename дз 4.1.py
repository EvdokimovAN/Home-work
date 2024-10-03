import numpy as np
import matplotlib.pyplot as plt
x = [10, 25, 35, 40, 45, 50, 60, 80]
y = [20, 40, 30, 37, 30, 40, 32, 60]
plt.plot(x,y, color = 'purple', marker = "o", markersize = 5)
plt.title('stonks')
plt.xlabel('время')
plt.ylabel('цены')
plt.grid(True, which='both', axis='both', linestyle='dashed')
plt.show()