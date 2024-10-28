class File:
    def __init__(self, capacity:int):
        self.size = 0
        self.tab = [None] * capacity
        self.capacity = capacity
        self.head = 0

    #j'enfile des élèments
    def enfile(self, value):
        if self.size < self.capacity:
            self.tab[(self.size+self.head)%self.capacity] = value
            self.size += 1
    #je défile les élèments
    def pop(self):
        value = self.tab[self.head]
        self.head = (self.head + 1)%self.capacity
        self.size -= 1
        return value

    def display(self):
        print("[", end="")
        for i in range(self.size):
            print(self.tab[(self.head+i)%self.capacity], end=", ")
        print("]")

ma_list = File(4)

ma_list.enfile(0)
ma_list.enfile(5)
ma_list.enfile(1)
ma_list.enfile(7)
ma_list.display()

ma_list.pop()
ma_list.display()