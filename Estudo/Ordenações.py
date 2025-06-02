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
    n = len(arr)

    if n < 2:  # Caso base da recursão: array com 0 ou 1 elemento já está ordenado
        return arr

    meio = n // 2  # Encontra o ponto médio para dividir o array
    
    # Chamadas recursivas para ordenar as duas metades
    left = merge_sort(arr[:meio])  # Metade esquerda
    right = merge_sort(arr[meio:]) # Metade direita
    
    new_arr = []  # Lista para armazenar o resultado da mesclagem
    l = r = 0     # Ponteiros para as listas 'left' e 'right'
    
    # Loop principal de mesclagem: compara elementos das duas listas
    while l < len(left) and r < len(right):
        if left[l] <= right[r]: # Se o elemento da esquerda for menor ou igual
            new_arr.append(left[l]) # Adiciona à nova lista
            l += 1 # Avança o ponteiro da lista esquerda
        else: # Se o elemento da direita for menor
            new_arr.append(right[r]) # Adiciona à nova lista
            r += 1 # Avança o ponteiro da lista direita
            
    # Adiciona quaisquer elementos restantes da lista 'left' (se houver)
    while l < len(left):
        new_arr.append(left[l])
        l += 1
        
    # Adiciona quaisquer elementos restantes da lista 'right' (se houver)
    while r < len(right):
        new_arr.append(right[r])
        r += 1
        
    return new_arr # Retorna a lista mesclada e ordenada

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


if __name__ == "__main__":
    lista = [10,9,8,7,6,5,4,3,2,1]
    print("Lista original:", lista)
    print("Lista ordenada:", merge_sort(lista))