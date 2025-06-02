import random
import time
import matplotlib.pyplot as plt

# Algoritmos de ordenação
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    # Mediana de três para escolher o pivô
    first, mid, last = arr[0], arr[len(arr)//2], arr[-1]
    pivot = sorted([first, mid, last])[1]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Função para comparar os algoritmos
def compare_sorting_algorithms():
    sizes = [1000, 10000, 20000, 30000, 40000, 50000]
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Selection Sort": selection_sort,
        "Merge Sort": merge_sort,
        "Quick Sort (Mediana de 3)": quick_sort,
    }
    results = {name: [] for name in algorithms}

    # Teste com listas aleatórias
    for size in sizes:
        arr = [random.randint(0, 1000) for _ in range(size)]
        for name, sort_func in algorithms.items():
            arr_copy = arr.copy()
            start_time = time.time()
            sort_func(arr_copy)
            end_time = time.time()
            results[name].append(end_time - start_time)
            print(f"{name} - Size {size}: {end_time - start_time:.4f}s")

    # Plotagem dos resultados (listas aleatórias)
    plt.figure(figsize=(12, 6))
    for name, times in results.items():
        plt.plot(sizes, times, label=name, marker='o')
    plt.xlabel("Tamanho da Lista")
    plt.ylabel("Tempo (s)")
    plt.title("Comparação de Algoritmos de Ordenação (Listas Aleatórias)")
    plt.legend()
    plt.grid()
    plt.show()

    # Teste com lista decrescente de 50.000 elementos
    descending_list = list(range(50000, 0, -1))
    descending_results = {}
    for name, sort_func in algorithms.items():
        arr_copy = descending_list.copy()
        start_time = time.time()
        if name == "Counting Sort":
            sorted_arr = sort_func(arr_copy)
        else:
            sort_func(arr_copy)
        end_time = time.time()
        descending_results[name] = end_time - start_time
        print(f"{name} (Lista Decrescente): {end_time - start_time:.4f}s")

    # Plotagem comparativa (50k aleatório vs. decrescente)
    plt.figure(figsize=(10, 6))
    names = list(descending_results.keys())
    times_random = [results[name][-1] for name in names]  # Último tamanho (50k)
    times_desc = list(descending_results.values())
    x = range(len(names))
    plt.bar(x, times_random, width=0.4, label="Lista Aleatória (50k)")
    plt.bar([i + 0.4 for i in x], times_desc, width=0.4, label="Lista Decrescente (50k)")
    plt.xticks([i + 0.2 for i in x], names, rotation=45)
    plt.ylabel("Tempo (s)")
    plt.title("Comparação: Lista Aleatória vs. Decrescente (50k elementos)")
    plt.legend()
    plt.grid(axis='y')
    plt.show()

compare_sorting_algorithms()