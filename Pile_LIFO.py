class Pile:
    def __init__(self, capacity:int):
        self.size = 0
        self.tab = [None] * capacity
        self.capacity = capacity
        self.head = 0

    #j'empile des élèments
    def push(self, value):
        #je vérifie d'abord si la pile est pleine je fais rien
        if self.size == self.capacity :
            return
        #sinon j'ajoute un element et puis j'incrèmente vers l'èlèment suivant
        else:
            self.tab[self.size] = value
            self.size += 1
    #je dépile des élèments
    def pop(self):
        self.size -= 1
        return self.tab[self.size]

    def display_from_top(self):
            #affichage depuis le dessus
            for i in range(self.size -1, -1, -1):
                if self.tab[i] is not None:
                    print(self.tab[i])

    def display_from_bottom(self):
            #affichage depuis le fond
            for i in range(self.size):
                if self.tab[i] is not None:
                    print(self.tab[i])

    def size(self, taille):
        #retourner la taille de la pile
        taille = self.tab[self.size]
        return taille

ma_liste = Pile(4)

ma_liste.push(2)
ma_liste.push(1)
ma_liste.push(3)
ma_liste.push(5)
ma_liste.display_from_top()
print()
ma_liste.pop()
ma_liste.display_from_top()
print()
print(ma_liste.size)