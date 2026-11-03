
import time
import random
import matplotlib.pyplot as plt

def bubble_sort(lista):
    a = lista.copy()
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def insertion_sort(lista):
    a = lista.copy()
    for i in range(1, len(a)):
        clave = a[i]
        j = i - 1
        while j >= 0 and a[j] > clave:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = clave
    return a

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izq = merge_sort(lista[:medio])
    der = merge_sort(lista[medio:])
    return merge(izq, der)

def merge(izq, der):
    resultado = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado

def medir(func, lista, reps=5):
    tiempos = []
    for _ in range(reps):
        inicio = time.time()
        func(lista.copy())
        tiempos.append(time.time() - inicio)
    return sum(tiempos) / len(tiempos)

n_valores = [1000, 2000, 3000, 4000]
algoritmos = {
    "Bubble": bubble_sort,
    "Insertion": insertion_sort,
    "Merge": merge_sort,
    "sorted()": sorted,
}

resultados = {nombre: [] for nombre in algoritmos}

for n in n_valores:
    lista = [random.randint(0, 10000) for _ in range(n)]
    for nombre, func in algoritmos.items():
        t = medir(func, lista)
        resultados[nombre].append(t)

print(f"{'n':>6} | " + " | ".join(f"{k:>12}" for k in algoritmos))
print("-" * (9 + 15 * len(algoritmos)))
for i, n in enumerate(n_valores):
    fila = f"{n:>6} | "
    fila += " | ".join(f"{resultados[k][i]:>11.6f}s" for k in algoritmos)
    print(fila)

plt.figure(figsize=(10, 6))
for nombre in algoritmos:
    plt.plot(n_valores, resultados[nombre], marker="o", label=nombre)
plt.xlabel("Tamaño de entrada (n)")
plt.ylabel("Tiempo (segundos)")
plt.title("Comparación de complejidad algorítmica")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("complejidad.png", dpi=120)
plt.show()