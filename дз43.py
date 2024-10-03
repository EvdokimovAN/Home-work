import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y = [50, 40, 30, 20, 10, 5, 10, 20, 30, 40, 50]
plt.bar(x,y, label='гистограмма', color = 'purple', alpha=0.5)
plt.title('гистограмма')
plt.xlabel('x')
plt.ylabel('y')
ax = plt.gca()
ax.set_xlim(0, 11)
ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
ax.set_yticks([0, 10, 20, 30, 40, 50, 60])
plt.legend(loc='lower right')
plt.show()