class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # Adicionei o prev que estava faltando

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def appendFinal(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def appendInicio(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def removeFinal(self):
        if self.is_empty():
            print("A lista está vazia")
            return None
        data = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return data

    def removeInicial(self):
        if self.is_empty():
            print("A lista está vazia")
            return None
        data = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return data

    def remover_duplicatas(self):
        if self.is_empty():
            return

        current = self.head
        while current is not None:
            runner = current.next
            while runner is not None:
                next_node = runner.next  # Guarda referência antes de possivelmente remover
                if runner.data == current.data:
                    # Atualiza o next do nó anterior
                    runner.prev.next = runner.next
                    self.size -= 1
                runner = next_node 
            current = current.next

    def display(self):
        current = self.head
        while current is not None:
            print('Conteúdo:', current.data)
            print('------------------------')
            current = current.next


lista = DLinkedList()
lista.appendInicio(1)
lista.appendInicio(2)
lista.appendInicio(3)
lista.appendInicio(2)
lista.appendInicio(4)
lista.appendInicio(1)

print("Lista original:")
lista.display()

lista.remover_duplicatas()

print("\nLista após remoção de duplicatas:")
lista.display()