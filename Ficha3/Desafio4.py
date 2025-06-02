def target_brute(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return True
    return False

# O(n²) (quadrática), pois percorre todos os pares possíveis com dois loops aninhados.

def target_optimizado(arr, target):
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    return False

#O(n) (linear), pois percorre a lista apenas uma vez e usa um conjunto (set) para verificações em tempo constante O(1).

arr = [1, 4, 6, 9, 12]
target = 10

print(target_optimizado(arr, target))  # Saída: True (1 + 9 = 10)
print(target_brute(arr, target))    # Saída: True