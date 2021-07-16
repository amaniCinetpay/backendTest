
#-----------------------Problème 1---------------------------------------
# La fonction pour avoir le nombre d'occurence des mots de Alice
def count_word(book,word):
    return book.count(word)
#------------------------------------------------------------------------




#-----------------------Problème 2---------------------------------------
# La fonction pour avoir le nombre d'occurence des lettres de Alice
def count_letter(word) :
    a = {i : word.count(i) for i in set(word)}
    return str(a).replace(": ","").replace("{","[").replace("}","]")
#------------------------------------------------------------------------


#-----------------------Problème 3---------------------------------------
# Etant donné que la bloucle "FOR" est appliquée une seule fois  dans le problème 2 sur un tableau 
# de n dimensions, nous déduisons que la complexité de la  fonction ci-dessus est de n 
#------------------------------------------------------------------------