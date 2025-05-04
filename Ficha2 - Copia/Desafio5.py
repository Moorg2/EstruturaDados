from collections import deque
class PilhaDeque:
    def __init__(self):
        self.pilha = deque()

    def push(self, elemento):
        self.pilha.append(elemento)

    def pop(self):
        if self.pilha is not None:
            return self.pilha.pop()
        else:
            return None

    def peek(self):
        if self.pilha is not None:
            return self.pilha[-1]
        else:
            return None

    def is_Empty(self):
        return len(self.pilha) == 0


class Node():
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class Stack():
    def __init__(self):
        self.head = None

    def push1(self, valor):
        node = Node(valor)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def pop1(self):
        if self.head is None:
            return None
        else:
            head = self.head
            self.head = self.head.next
            return head.valor

    def isEmpty1(self):
        if self.head is None:
            return True
        return False

    def peek1(self):
        if self.head is None:
            return None
        return self.head.valor



pilha = PilhaDeque()
pilha.push(5)
pilha.push(10)
pilha.push(15)
pilha.push(20)
print(pilha.is_Empty())
print(pilha.peek())
print(pilha.pop())
print(pilha.peek())
print(pilha.is_Empty())


#Nas minhas considerações finais eu diria que o deque utilizando os metodos nativos do phyton trazem mais eficiencia no programa. Afinal os problemas de ponteiro, seus valores, são atualizados instantaneamente pelo programa. 