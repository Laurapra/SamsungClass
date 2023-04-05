#quiz en parejas
class Deque:
    def __init__(self):
        self.queue = []

    def add_first(self, item):
        '''Agregar un elemento al principio de la cola'''
        self.queue.insert(0, item)

    def remove_first(self):
        '''Quitar y devolver el artículo desde el principio'''
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return None

    def add_last(self, item):
        '''Agregar un elemento al lado trasero de la cola'''
        self.queue.append(item)

    def remove_last(self):
        '''Quitar y devolver el artículo del lado trasero'''
        if len(self.queue) > 0:
            return self.queue.pop()
        else:
            return None
d = Deque()
d.add_first(1)
d.add_last(2)
d.add_first(3)
d.add_last(4)
print(d.remove_first())  # Output: 3
print(d.remove_last())   # Output: 4
print(d.remove_first())  # Output: 1
print(d.remove_last())   # Output: 2
