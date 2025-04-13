from timeit import default_timer as timer
import matplotlib.pyplot as plt

def logarithms(n):
    i = 1
    values = []  # Lista para guardar los valores de i
    times = []   # Lista para guardar los tiempos acumulados
    start = timer()  # Inicia la medición del tiempo
    
    while i <= n:
        values.append(i)  # Guarda el valor actual de i
        
        # Medimos el tiempo transcurrido en cada iteración
        elapsed_time = timer() - start
        times.append(elapsed_time)  # Guarda el tiempo transcurrido
        
        i *= 2  # Multiplicamos i por 2 para la progresión logarítmica
    
    return values, times  # Retorna los valores de i y sus tiempos acumulados

# Definir el valor de n
n = 10 ** 3

# Ejecutar la función y obtener los datos
values, times = logarithms(n)

# Graficar los datos
plt.scatter(values, times, color="Red")
plt.plot(values, times, linestyle='dashed', color='blue')  # Línea para mejor visualización
plt.title('Logarithmic Complexity')
plt.xlabel('n values')
plt.ylabel('Time (seconds)')
plt.xscale('log')  # Escala logarítmica para una mejor visualización
plt.grid(False)  # Agregar una cuadrícula para mayor claridad
plt.show()
