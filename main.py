from Trie import Trie


def main():

########## NAIVE SOLUTION
    def check_words(word: str) -> bool:  #fonction qui vérifie si un mot est dans le dico
        dico =[]
        return word in dico

    def checkSentence() -> bool:

        sentence = input("Rentrez la phrase : ")
        sentenceTab = sentence.split()
        for word in sentenceTab:
            if not check_words(word):
                return False

        return True

    def initialiseDico():
        dico = []
        with open("dico.txt", encoding='utf-8') as file:
            for row in file:
                try:
                    dico.append(row.strip())
                except:
                    print("Ligne buguée")
        return dico
#######################################

    graph = Trie()

    with open("dico.txt", encoding='utf-8') as file:
        for row in file:
            try:
                graph.insert(row.strip())
            except:
                print("Ligne buguée")



if __name__ == '__main__':
    main()
