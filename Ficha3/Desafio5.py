#Letra A:
#A complexidade algorítmica determina como o tempo de execução e o uso de recursos crescem conforme o tamanho da entrada (ex: número de endereços de entrega).
#A questão do tempo: Se o algoritmo tem complexidade exponencial (O(2^n)), uma lista com 100 endereços se torna intratável.
#Custos operacionais elevados: Algoritmos O(n³) ou O(n!) consomem muita CPU e energia, inviabilizando operações em tempo real.
#A realidade de uma empresa em desenvolvimento: Empresas em crescimento precisam de algoritmos que lidem bem com aumento de demanda (ex: O(n log n) ou O(n)).


#Letra B
#A notação Big O nos ajuda a comparar algoritmos abstratamente, sem depender de implementações específicas ou a capacidade computacional de máquinas diferentes. Com ela, conseguimos prever qual algoritmo será mais eficiente à medida que o número de entregas cresce.
#Por exemplo um algoritmo de força bruta que testa todas as permutações de entrega (O(n!)) pode levar minutos ou horas para calcular a melhor rota com 15 paradas.
# Combine com técnicas de clusterização (agrupar entregas por região) para reduzir complexidade.