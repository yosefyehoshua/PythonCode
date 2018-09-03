class Node:
    def __init__(self, data=None):
        self.__data = data
        self.__prev = None
        self.__next = None

    def get_data(self):
        return self.__data

    def get_prev(self):
        return self.__prev

    def get_next(self):
        return self.__next

    def set_prev(self, prev):
        self.__prev = prev

    def set_next(self, next):
        self.__next = next


class DualLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__len = 0

a = [0,1,2,3,4,5]



def iter(c):
    lenn = 3
    idx = 0
    float = c/10**(lenn-1)
    while idx < lenn:
        yield int(float)
    float = float - int(float) * 10


c = 432
print(next(iter(432)))

print(next(iter(432)))
print(next(iter(432)))