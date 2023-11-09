import matplotlib.pyplot as plt
import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Testando os algoritmos com diferentes tamanhos de arrays
sizes = [100, 200, 300, 400, 500]
bubble_times = []
quick_times = []

for size in sizes:
    arr = [random.randint(0, 1000) for _ in range(size)]

    # Teste para Bubble Sort
    arr_copy = arr.copy()
    start_time = time.time()
    bubble_sort(arr_copy)
    bubble_times.append(time.time() - start_time)

    # Teste para Quick Sort
    arr_copy = arr.copy()
    start_time = time.time()
    quick_sort(arr_copy)
    quick_times.append(time.time() - start_time)

# Plotando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(sizes, bubble_times, label='Bubble Sort', marker='o')
plt.plot(sizes, quick_times, label='Quick Sort', marker='o')
plt.title('Comparação do Tempo de Execução: Bubble Sort vs Quick Sort')
plt.xlabel('Tamanho do Array')
plt.ylabel('Tempo de Execução (s)')
plt.legend()
plt.grid(True)
plt.show()
