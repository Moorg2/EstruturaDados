# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AYR1EKQsAT6bp6Qy7mGwUQjIfAgtMNiA
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

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

    def removeFinal(self,data):
        if self.is_empty():
          print("A lista está vazia")
        else:
          data = self.tail.data
          self.tail = self.tail.prev
          self.tail.next = self.tail.next.next
          self.size -= 1

    def removeInicial(self,data):
        if self.is_empty():
          print("A lista está vazia")
        else:
          data = self.head.data
          self.head = self.head.next
          self.head.prev = self.head.prev.prev
          self.size -= 1

#Eu prefiri fazer uso de uma double linked list pois suas caracteristicas de um head e tail definidos facilitam a inserção e retirada de elesmentos no começo e no final da lista