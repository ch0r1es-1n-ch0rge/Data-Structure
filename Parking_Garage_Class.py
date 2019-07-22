class Garage:
    __MaxQueue = 0
    __items = []
    __front = -1
    __rear = -1
    __length = 0

    def __init__(self, size):
        self.__MaxQueue = size + 1
        self.__items = [None] * self.__MaxQueue
        self.clear()

    def clear(self):
        self.__front = self.__MaxQueue - 1
        self.__rear = self.__MaxQueue - 1
        self.__length = 0

    def is_empty(self):
        if self.__rear == self.__front:
            return True
        else:
            return False

    def is_full(self):
        if (self.__rear + 1) % self.__MaxQueue == self.__front:
            return True
        else:
            return False

    def insert(self, item):
        self.__rear = (self.__rear + 1) % self.__MaxQueue
        self.__items[self.__rear] = item
        self.__length += 1

    def delete(self):
        self.__front = (self.__front + 1) % self.__MaxQueue
        self.__length -= 1
        return self.__items[self.__front]

    def size_of_queue(self):
        return self.__length

    def capacity_of_queue(self):
        return self.__MaxQueue - 1
