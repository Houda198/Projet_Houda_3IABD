def hash(chaine):
    sum = 0
    for i in chaine:
        # ord renvoie le nbr ascii de chaque caractere
        sum += ord(i)
    return sum
class HashMap:
    def __init__(self, size):
        self.size = size
        self.value = [list() for _ in range(self.size)]

#fonction hashage

    def add(self, word):
        index = hash(word) % self.size
        if word not in self.value[index]:
            self.value[index].append(word)

    def contains(self, word):
        index = hash(word) % self.size
        return word in self.value[index]

    def remove(self, word):
        index = hash(word) % self.size
        if word in self.value[index]:
            self.value[index].remove(word)

    def display(self):
        for i in range(self.size):
            print(self.value[i])


if __name__ == "__main__":
    hashmap = HashMap(6)
    hashmap.add("hi")
    hashmap.add("today")
    print(hashmap.contains("houda"))
    hashmap.display()
    hashmap.remove("hi")
    hashmap.display()





