def quicksort_mediana_de_tres(arr, low, high):
    if low < high:
        # Particiona o array e obtém o índice do pivô
        pivot_index = partition_mediana_de_tres(arr, low, high)
        # Recursivamente ordena as partições
        quicksort_mediana_de_tres(arr, low, pivot_index - 1)
        quicksort_mediana_de_tres(arr, pivot_index + 1, high)

def partition_mediana_de_tres(arr, low, high):
    # Encontra os índices do início, meio e fim
    mid = (low + high) // 2

    # Ordena os três elementos para encontrar a mediana
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]

    # Usa a mediana (que agora está no índice 'mid') como pivô
    arr[mid], arr[high] = arr[high], arr[mid]
    pivot = arr[high]

    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Coloca o pivô na posição correta
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Exemplo de uso
lista = [33, 10, 55, 71, 29, 3, 18, 45]
print("Antes:", lista)
quicksort_mediana_de_tres(lista, 0, len(lista) - 1)
print("Depois:", lista)


#O Quick Sort é um dos algoritmos de ordenação mais eficientes na prática, com complexidade média de tempo O(n log n). No entanto, no pior caso, sua complexidade pode ser O(n²), esse caso é quando o pivô escolhido é o menor ou maior elemento em um vetor já ordenado ou quase ordenado. Isso causa partições extremamente desbalanceadas.

#O algoritmo faz uso de um valor mediano alcançado pela divisão dos itens de indice 0 e -1(ultimo item da lista) como pivô. Isso geralmente leva a partições mais equilibradas, evitando o pior caso com mais frequência.