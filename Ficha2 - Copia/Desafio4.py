class Node():
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class Stack():
    def __init__(self):
        self.head = None

    # Inserindo valor na primeira casa (topo da pilha)
    def push(self, valor):
        node = Node(valor)
        node.next = self.head
        self.head = node

    # Remover valor do topo da pilha
    def pop(self):
        if self.head is None:
            return None
        current = self.head
        self.head = self.head.next
        return current.valor

    def isEmpty(self):
        return self.head is None

    def size(self):
        if self.isEmpty():
            return 0
        current = self.head
        size = 1
        while current.next is not None:
            size += 1
            current = current.next
        return size

    def peek(self):
        if self.head is None:
            return None
        return self.head.valor

    def clear(self):
        self.head = None

    # Método para inverter a pilha
    def inverter_pilha(self):
        pilha_auxiliar = Stack()
        
        # Passo 1: Desempilhar tudo da pilha original para a pilha auxiliar
        while not self.isEmpty():
            pilha_auxiliar.push(self.pop())
        
        # Passo 2: Repassar os dados de volta para a pilha original
        while not pilha_auxiliar.isEmpty():
            self.push(pilha_auxiliar.pop())

    def display(self):
        current = self.head
        while current is not None:
            print(current.valor)
            current = current.next

# Criando a pilha
pilha = Stack()

# Inserindo elementos na pilha
for valor in [4, 's', 'v', 'y', 2, 3]:
    pilha.push(valor)

print("Pilha original:")
pilha.display()

# Invertendo a pilha
pilha.inverter_pilha()

print("\nPilha invertida:")
pilha.display()
