import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('datos_primera.txt')
plt.figure()
plt.scatter(data[:,0], data[:,1], label = 'Numerico')
plt.plot(data[:,0], np.exp(-data[:,0]), label = 'Analitica')
plt.legend()
plt.savefig("grafica_primera.pdf")
