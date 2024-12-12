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
    def contains(self, word):
        index = hash(word)
        count = 0
        while self.value [(index + count) % self.size] != "":
            if self.value[(index + count) % self.size] == word:
                return True
            count += 1
        return False

    def remove(self, word):
        index = hash(word)
        count = 0
        remove = False
        while self.value [(index + count) % self.size] != "":
            if self.value[(index + count) % self.size] == word:
                remove = True
                self.value[(index + count) % self.size] = ""
                break
            count += 1
        if remove and self.value [(index + count + 1) % self.size] != "":
            copy = self.value
            self.value = ["" for _ in range(self.size)]
            for word in copy:
                if word != "":
                    self.add(word)


    def display(self):
            print(self.value)

hashmap = HashMap(3)
hashmap.add("houda")
hashmap.add("empathic")
hashmap.add("empathik | laaslama  | akham ")
hashmap.display()
print(hashmap.contains("empathic"))
hashmap.display()
print(hashmap.contains("greenLand"))
hashmap.remove("empathic")
hashmap.display()