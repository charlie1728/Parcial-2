
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        # self.infectado = False
        # self.hits = 0

    def __str__(self):
        # estado = " 🦠[Infectado]" if self.infectado else ""
        return f"Node({self.data!r})" 

    