class Stack:
    def __init__(self):
        self.max_items = 100
        self.items = [] * self.max_items
        self.top = -1

    def clear(self):
        self.items.clear()

    def is_empty(self):
        if not self.items:
            return True
        else:
            return False

    def is_full(self):
        if self.top == self.max_items - 1:
            return True
        else:
            return False

    def push(self, item):
        self.items.append(item)

    def pop(self):
        del self.items[self.top]
        # self.items -= 1

    def top_stack(self):
        return self.items[self.top]

    def size(self):
        return len(self.items)

    def capacity(self):
        return self.max_items
