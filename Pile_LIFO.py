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
            self.tab[self.head] = value
            self.size += 1
    #je dépile des élèments
    def pop(self, value):
        if self.size == self.capacity :
            return self.tab[self.head]
        else:
            self.tab[self.head] = value
            self.size -= 1

            return self.tab[self.head]

    def display(self):
            #affichage depuis le dessus
            for i in range(self.size):
                i-=1
                if self.tab[i] is not None:
                    print("%d ", self.tab[i])

            #affichage depuis le fond
            for i in range(self.size):
                i+=1
                if self.tab[i] is not None:
                    print("%d " % self.tab[i])

    def browse(self, value):
        #je vérifie si le premier elem de la pile est nul, je retourne nul
        if self.head is None:
            return None
        #sinon je retourne le 1er elem de la pile
        else :
            value =  self.head.value

    def size(self, taille):
        #retourner la taille de la pile
        taille = self.tab[self.size]
        return taille

ma_liste = Pile(4)

ma_liste.push(2)
ma_liste.push(1)
ma_liste.push(3)
ma_liste.push(5)
ma_liste.display()

ma_liste.pop(3)
ma_liste.display()
