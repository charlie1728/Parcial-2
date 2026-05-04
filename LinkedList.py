from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def agregar(self, data):
        nuevo = Node(data)
        if not self.head:
            self.head = nuevo
            self.tail = nuevo
            return
        actual = self.head
        while actual.next:
            actual = actual.next
        actual.next = nuevo
        self.tail = nuevo

 

# ── PRUEBAS ──────────────────────────────────────
lista1 = LinkedList()
# for n in [1, 2, 3, 4, 5]:
#     lista1.agregar(n)
# lista2 = LinkedList()
# for n in [21, 4, 6, 8]:
#     lista2.agregar(n)

# actual = lista1.head
# while actual:
#     print(actual, end=" -> " if actual.next else " -> None\n")
#     actual = actual.next




