import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('datos_segunda.txt')
plt.figure()
plt.scatter(data[:,0], data[:,1], label = 'Numerico')
plt.plot(data[:,0], np.cos(data[:,0]), label = 'Analitica')
plt.legend()
plt.savefig("grafica_segunda.pdf")

plt.figure()
plt.scatter(data[:,1], data[:,2])
plt.savefig("z_funcion_y.pdf")
