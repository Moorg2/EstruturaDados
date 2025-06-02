def counting_sort(array, max_val):
    # 1. Inicializa um array de contagem com zeros
    count = [0] * (max_val + 1)
    
    # 2. Conta a frequência de cada elemento no array original
    for num in array:
        count[num] += 1
    
    # 3. Modifica o array de contagem para acumular as posições
    for i in range(1, max_val + 1):
        count[i] += count[i - 1]
    
    # 4. Constrói o array ordenado
    sorted_array = [0] * len(array)
    for num in reversed(array):  # Percorre do fim para manter estabilidade
        sorted_array[count[num] - 1] = num
        count[num] -= 1
    
    return sorted_array


