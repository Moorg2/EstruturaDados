{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOxi90yjbdGlalH0CBlwXJu"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 18,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mgvHyNaeBRF4",
        "outputId": "666945b5-7826-4b76-bdef-d9494d809838"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Lista original:\n",
            "Conteúdo: 1\n",
            "------------------------\n",
            "Conteúdo: 2\n",
            "------------------------\n",
            "Conteúdo: 3\n",
            "------------------------\n",
            "Conteúdo: 2\n",
            "------------------------\n",
            "Conteúdo: 4\n",
            "------------------------\n",
            "Conteúdo: 1\n",
            "------------------------\n",
            "\n",
            "Lista após remoção de duplicatas:\n",
            "Conteúdo: 1\n",
            "------------------------\n",
            "Conteúdo: 2\n",
            "------------------------\n",
            "Conteúdo: 3\n",
            "------------------------\n",
            "Conteúdo: 4\n",
            "------------------------\n"
          ]
        }
      ],
      "source": [
        "class Node:\n",
        "    def __init__(self, data):\n",
        "        self.next = None\n",
        "        self.data = data\n",
        "\n",
        "class LinkedList:\n",
        "    def __init__(self):\n",
        "        self.head = None\n",
        "\n",
        "    def append(self, data):\n",
        "        new_node = Node(data)\n",
        "        if self.head is None:\n",
        "            self.head = new_node\n",
        "        else:\n",
        "            current = self.head\n",
        "            while current.next is not None:\n",
        "                current = current.next\n",
        "            current.next = new_node\n",
        "\n",
        "    def display(self):\n",
        "        current = self.head\n",
        "        while current is not None:\n",
        "            print('Conteúdo:', current.data)\n",
        "            print('------------------------')\n",
        "            current = current.next\n",
        "\n",
        "    def remover_duplicatas(self):\n",
        "        if self.head is None:\n",
        "          print(\"A lista está vazia\")\n",
        "\n",
        "        visto = set()\n",
        "        current = self.head\n",
        "        anterior = None\n",
        "\n",
        "        while current is not None:\n",
        "            if current.data in visto:\n",
        "                anterior.next = current.next\n",
        "            else:\n",
        "                visto.add(current.data)\n",
        "                anterior = current\n",
        "            current = current.next\n",
        "\n",
        "\n",
        "\n",
        "lista = LinkedList()\n",
        "lista.append(1)\n",
        "lista.append(2)\n",
        "lista.append(3)\n",
        "lista.append(2)\n",
        "lista.append(4)\n",
        "lista.append(1)\n",
        "\n",
        "print(\"Lista original:\")\n",
        "lista.display()\n",
        "\n",
        "lista.remover_duplicatas()\n",
        "\n",
        "print(\"\\nLista após remoção de duplicatas:\")\n",
        "lista.display()\n"
      ]
    }
  ]
}