# LDC
## Class Cell 
Cette classe represente une case de ma liste chaînée
## Class MyList
cette classe sert à initialiser ma liste chaînée
## Insert_next
Cette fonction sert à insérer l'elément à la suite de la liste, elle prend en paramètres les attributs self, value et la classe Cell. Je vérifie si la liste est vide on donne la valeur new_element pour la première cell de la liste, je faire l'insertion quand la liste n'est pas vide,si la cell n'a pas de valeur suivante je crée un (nouveau) new_element qui est dernier de la liste,sinon on créée une nouvelle cell entre 2 cells et mettre à jour
## Insert_previous 
Cette fonction vérifie d'abord si la liste n'est pas vide, puis j'insère l'élément avant l'élément passé en paramètres,je crée mon nouvel élément enn insérnant sa valeur,je vérifie si la liste est vide,je rajoute un élément qui sera head et tail de ma liste,si j'ai rien avant element j'insère un element avant le head d'ou changer la valeur du head, sinon je relie l'element precedent avec le nouvel element, le nouvel  element se place avant l'element passé en paramètres.
## remove
dans cette fonction, je vérifie si mon element est au début, dans le cas où je supprime le premier element, le premier element devint deuxieme de la liste, si en décalant le premier element à la deuxième place et que cet element est None, ça veut dire qu'il y a qu'un seul element dans la liste en supprimant la fin de la liste,dans le cas où je veux supprimer un autre element à part le premier, si l'element d'après est None le tail de la liste devint l'avant dernier element 
## display
cette fonction affiche l'ensemble des valeurs de ma liste
# Binary_tree 
## Class Node 
cette classe represente une feuille d'un arbre 
## Insert
cette fonction insere les elements dans un arbre selon leurs valeurs, s'il est supérieur à la valeur en paramètres il va à droite de l'arbre sinon il va à gauche de l'arbre 
## in_order_traversal
cette fonction sert à lire les elements de l'arbre du plus bas à gauche montant jusqu'à la racine puis parcours la branche droite du bas jusqu'en haut 
## pre_order_traversal
cette fonction sert à afficher d'abord la racine puis parcours la branche gauche puis celle de la droite 
## post_order_traversal
cette fonction parcours la branche gauche du bas et ça monte jusqu'en haut puis parcours la branche droite et ça remonte jusu'à la racine et finit par l'affichage de cette derniere 
## search
cette fonction sert à chercher un element dans un arbre, dans un premier temps on parcours la branche gauche (value<self.value), si on trouve toujours pas la valeur cherchée on parcours la branche droite (value > self.value), si on tombe sur un None ça renvoie 0 sinon ça renvoie 1
## Find_Min
cette fonction sert à chercher le minimum dans un arbre qui se trouve au plus bas de la branche gauche de l'arbre 
## Find_Max
cette fonction sert à chercher le maximum dans un arbre qui se trouve au plus bas de la branche droite de l'arbre 
## delete
cette fonction sert à supprimer l'element en parametres, on parcours les deux branches, puis si l'element n'a pas de fils ça renvoie un None, s'il a 1 seul fils ça le renvoie (soit gauche ou droit), s'il a 2 fils, on parcourt la branche à droite en quête du minimum de l'arbre droit par lequel l'element est remplacé, et par la suite on supprime le minimum de l'arbre droit
## breadth
cette fonction sert au parcours de l'arbre du haut jusqu'en bas et de gauche à droite (ligne par ligne)
## treeSize
cette fonction sert à calculer le nombre d'elements dans un arbre (feuilles + 1)
## treeHeight
cette fonction sert à compter le nombre de lignes dans un arbre, en parcourant le sous-arbre gauche puis le sous-arbre droit et après il compare les 2 sous-arbres et renvoie le plus haut + 1
## leefsCount
cette fonction sert à calculer le nombre de feuilles dans un arbre, le nobre total d'elements sans aucun fils
# file_FIFO
## Class file
cette classe sert à initiliser une liste vide d'une certaine capacité
## enfile
cette fonction sert à enfiler des elements dans la liste, si le nombre d'elements est < à la capacité de la liste, ça le met dans le tableau dans l'emplacement qui le correspond 
## pop
cette fonction sert à défiler le premier element de la file 
## display
cette fonction sert à afficher les elements de la file du début jusqu'à la fin 
# pile_LIFO
## Class Pile
cette classe sert à initialiser une liste vide d'une certaine capacité
## push
cette fonction sert à enfiler des elements dans la pile, je vérifie d'abord si la pile est pleine je fais rien,sinon j'ajoute un element et puis j'incrèmente vers l'èlèment suivant
## pop
cette fonction sert à dépiler les elements au dessus de la pile
## display_from_top
cette fonction sert à afficher les elements du haut en bas, commençant par la derniere case du tableau (qui est le 1er de la pile), s'arretant à 0, et avançant d'un pas = 1 
## display_from_bottom
cette fonction sert à afficher les elements du bas de la pile jusqu'en haut 
## size 
cette fonction sert à retourner la taille de la pile
# Hashage_ouvert
## Class HashMap
cette classe sert à initialiser une map d'une certaine size 
## hash
cette fontion sert à calculer les index de ma table hash, elle calcule la somme des nombres ASCII des chaînes de caractères 
## add
cette fonction sert à ajouter une chaîne de caractères dans la table de hash, je calcule d'abord l'index de la fonction hash et puis je l'ajoute au tableau selon l'index que j'ai.si un mot n'est pas dans son index approprié, je l'ajoute dedans 
## contains
cette fonction sert à vérifier si un mot quelconque est dans son index approprié
## remove
cette fonction sert à supprimer un mot qu'on a trouvé dans son index 
## dispaly
cette fonction sert à afficher toute la table de hashage
# Hashage_ferme
## Class HashMap
cette classe sert à initialiser une map d'une certaine size
## add
cette fonction sert à ajouter des elements dans la table d'hashage, je vérifie si à un index calculé y a aucum, j'ajoute ce dernier et je dis à ma map qu'il y a un mot en plus, si la hashmap est à moitié pleine, je double sa taille en recréant une nouvelle hashmap vide avec la même taille que celle que j'avais, et j'ajoute tous les mots dedans, et si la case est déjà remplie il passe à celle d'après jusqu'à ce qu'il tombe sur la case vide pour ajouter le mot
## contains
cette fonction vérifie si la hashmap contient un certain mot, tant que la case n'est pas vide, si je tombe sur le mot cherché ça renvoie true sinon il passe à, la case d'après 
## remove 
cette fonction sert à supprimer un mot de la hashmap,je vérifie si le mot existe, je le supprime et j'arrête de boucler, si je supprime un mot de la hashmap et que la case d'après est remplie, je recrée une nouvelle hashmap pour ranger tous les mots dedans.
## display
cette fonction sert à afficher les elements de ma hashmap.
# AVL
## Class Node
cette classe définit un element de l'arbre
## updateHeight
cette fonction sert à calculer la hauteur d'un arbre en fonction des nombre des niveaux dans l'arbre, et s'il y a deux fils il prend le plus haut + 1.
## getBalance
cette fonction sert à calculer l'équilibrage de l'arbre, si les fils existent ça renvoie la différence de la hauteur entre le droit et le gauche r-l,sinon (s'il y a aucun fils)la hauteur est de 0.
## find_max
cette fonction sert à chercher le maximum dans un arbre qui se trouve au plus bas de la branche droite de l'arbre 
## in_order_traversal
cette fonction sert à lire les elements de l'arbre du plus bas à gauche montant jusqu'à la racine puis parcours la branche droite du bas jusqu'en haut 
## insertNode
cette fonction sert à l'insertion d'un element en fonction de sa valeur si > ou < à la self value, puis je fais la mise à jour de la hauteur de l'arbre.
## deleteNode
cette fonction sert à supprimer l'element en parametres, on parcours les deux branches, puis si l'element n'a pas de fils ça renvoie un None,puis met à jour la hauteur de l'arbre, s'il a 1 seul fils ça le renvoie (soit gauche ou droit),puis met à jour la hauteur de l'arbre, s'il a 2 fils, on parcourt la branche à droite en quête du minimum de l'arbre droit par lequel l'element est remplacé,puis met à jour la hauteur de l'arbre, et par la suite on supprime le maximum de l'arbre gauche et puis met à jour la hauteur de l'arbre.
## LeftRotate
cette fonction sert à faire la rotation à gauche d'un arbre, je déplace la racine vers la gauche et le fils droit devient la nouvelle racine.
## RightRotate
cette fonction sert à faire la rotation à droite d'un arbre, je déplace la racine vers la droite et le fils gauche devient la nouvelle racine.
## Class AVL_tree
cette classe contient l'arbre AVL
## balance
cette fonction sert à rééquilibrer l'arbre, si la racine ou (le fils gauche & droit) n'esxiste pas on s'arrete, après je calcule le coefficient de l'équilibrage s'il est < -1 je calcule le coefficient du fils gauche s'il est positif je fais une rotation à gauche du fils gauche puis une rotation à droite au niveau de la racine, et le coefficient est > 1 je fais un e rotation à droite puis je calcule le coefficient du fils droit s'il est positif je tourne le fils droit vers la droiteet après je tourne la racine vers la gauche.
## insert
cette fonction appelle la fonction insert de la classe node puis fait l'équilibrage
## delete 
cette fonction appelle la fonction deldete de la classe node puis fait l'équilibrage
## display
cette fonction appelle la fonction in_order_traversal de la classe node pour afficher l'arbre.

