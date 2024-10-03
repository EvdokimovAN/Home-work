import numpy as np
import matplotlib.pyplot as plt
x = [49, 49, 2]
l = ['Не, я отдохну','Это тоже отдых, но другим цветом','Спать']
plt.pie(x, labels=l, autopct='%1.1f%%')
plt.title('Коллок скоро. Может поботать матан?')
plt.show()