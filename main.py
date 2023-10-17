from Trie import Trie
import time


def main():

########## NAIVE SOLUTION
    def check_words(dico,word: str) -> bool:  #fonction qui vérifie si un mot est dans le dico
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

    a = time.time()
    print(check_words(initialiseDico(),'coire'))
    b = time.time()
    c = b - a
    print(f"Execution time Naive: {c} seconds")
#######################################

    graph = Trie()

    with open("dico.txt", encoding='utf-8') as file:
        for row in file:
            try:
                graph.insert(row.strip())
            except:
                print("Ligne buguée")

    start_time = time.time()
    print(graph.checkWord('Coiffeur'))
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time Trie: {execution_time} seconds")

    graph.checkFile(file="./sentence")

if __name__ == '__main__':
    main()
