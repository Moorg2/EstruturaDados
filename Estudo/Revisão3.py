def insertion_sort_with_count(arr):
    comparisons = 0  # Contador de comparações
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Conta a comparação do while mesmo se não entrar no loop
        while j >= 0:
            comparisons += 1  # Conta a comparação (arr[j] > key)
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return comparisons

# Exemplo de uso:
vetor = [5, 2, 4, 6, 1, 3]
num_comparacoes = insertion_sort_with_count(vetor.copy())
print("Vetor ordenado:", vetor)
print("Número de comparações:", num_comparacoes)