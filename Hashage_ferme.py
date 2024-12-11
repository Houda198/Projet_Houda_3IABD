from Hashage_ouvert import hash
class HashMap:
    def __init__(self, size):
        self.size = size
        self.value = ["" for _ in range(self.size)]
        self.count = 0

    def add (self, word):
        index = hash(word) % self.size
        depart = index
        count = 0
        if word not in self.value:
            while count < self.size:
                if self.value[index] == "":
                    self.value[index] = word
                    self.count += 1
                    if self.count > self.size /2:
                        old_value = self.value
                        self.size *= 2
                        self.value = ["" for _ in range(self.size)]
                        self.count = 0
                        for word in old_value:
                            if word != "":
                                self.add(word)

                    return
                index = (index + 1) % self.size
                count +=1

    def display(self):
            print(self.value)

hashmap = HashMap(3)
hashmap.add("houda")
hashmap.add("empathic")
hashmap.add("empathik")
hashmap.display()

