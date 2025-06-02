class Carta:
    def __init__(self, nome):
        self.nome = nome
        
    def __repr__(self):
        return self.nome  # Para mostrar melhor as cartas

    @staticmethod
    def combinatoria(lista_cartas):
        todas_combinacoes = []
        n = len(lista_cartas)
        
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    combinacao = [lista_cartas[i], lista_cartas[j], lista_cartas[k]]
                    todas_combinacoes.append(combinacao)
        
        return todas_combinacoes


# Criando as cartas
Carta1 = Carta("Ogro")
Carta2 = Carta('Elfo')
Carta3 = Carta("Dragao")
Carta4 = Carta("Anao")
Carta5 = Carta("Mago")
cartas = [Carta1, Carta2, Carta3, Carta4, Carta5]

# Gerando e mostrando combinações
combinacoes = Carta.combinatoria(cartas)
for idx, comb in enumerate(combinacoes, 1):
    print(f"Combinação {idx}: {comb}")


# A) É criado uma classe com um construttor que receba nome, mana, vida, ataque, depois disso é criado um metodo que irá receber uma lista formada pelas cartas criadas. Esse metodo para a realização da combinação será formado por 3 for aninhadas para fazer com que a lista corra corretamente.
# B) A analise de complexidade do codigo será realizada levando em consideração a existencia dos 3 for aninhados, que colocam a complexidade em O(n³) de acordo com a notação de complexidade Big O. Existem 10 combinação possiveis.