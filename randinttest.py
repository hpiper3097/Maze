from random import randint, choice
import numpy as np
import matplotlib.pyplot as plt

#rali = [randint(1, 20) for x in range(99)]
#for n in range(10):
#    print(choice(rali))

npr = [np.linspace(2+x, 7+x, 6) for x in range(6)]

plt.pcolormesh(npr)
plt.show()