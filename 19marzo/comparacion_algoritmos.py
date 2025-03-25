import time
import random
"""
Explicación del Código:
Algoritmo O(n^2): Ordenamiento por selección:
    Recorre la lista n veces, y en cada iteración busca el mínimo en la sublista restante.
    Complejidad: O(n^2).

Algoritmo O(n log n): Ordenamiento por mezcla (Merge Sort):
    Divide la lista en dos mitades, las ordena recursivamente y luego las mezcla.
    Complejidad: O(n log n).

Medición de tiempo:
    Se utiliza la función time.time() para medir el tiempo de ejecución de cada algoritmo.
    Se crea una lista aleatoria de tamaño n = 10000 para probar ambos algoritmos.

Comparación:
    Se imprime el tiempo de ejecución de ambos algoritmos.
    Se muestra cuál es más rápido.

"""
# Algoritmo con complejidad O(n^2): Ordenamiento por selección
def ordenamiento_seleccion(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Algoritmo con complejidad O(n log n): Ordenamiento por mezcla (Merge Sort)
def ordenamiento_mezcla(arr):
    if len(arr) <= 1:
        return arr
    medio = len(arr) // 2
    izquierda = ordenamiento_mezcla(arr[:medio])
    derecha = ordenamiento_mezcla(arr[medio:])
    return mezclar(izquierda, derecha)

def mezclar(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

# Función para medir el tiempo de ejecución de un algoritmo
def medir_tiempo(algoritmo, arr):
    inicio = time.time()
    algoritmo(arr)
    fin = time.time()
    return fin - inicio

# Generar una lista aleatoria de tamaño n
n = 10000  # Tamaño de la lista
arr = [random.randint(1, 100000) for _ in range(n)]

# Medir tiempo del algoritmo O(n^2)
tiempo_seleccion = medir_tiempo(ordenamiento_seleccion, arr.copy())
print(f"Tiempo de ordenamiento por selección (O(n^2)): {tiempo_seleccion:.6f} segundos")

# Medir tiempo del algoritmo O(n log n)
tiempo_mezcla = medir_tiempo(ordenamiento_mezcla, arr.copy())
print(f"Tiempo de ordenamiento por mezcla (O(n log n)): {tiempo_mezcla:.6f} segundos")

# Comparación de tiempos
if tiempo_mezcla < tiempo_seleccion:
    print("El ordenamiento por mezcla es más rápido.")
else:
    print("El ordenamiento por selección es más rápido.")