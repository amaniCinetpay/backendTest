
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
