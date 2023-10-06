from TrieNode import TrieNode
import numpy as np


class Trie:

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        currentNode = self.root
        word = word.casefold()
        for i in range(len(word)):

            if word[i] not in currentNode.children:
                currentNode.children[word[i]] = TrieNode(word[i], i == len(word) - 1)
            elif i == len(word) - 1:
                currentNode.children[word[i]].is_end = True

            currentNode = currentNode.children[word[i]]

    def checkWord(self, word: str):
        curr = self.root
        word = word.casefold()
        def check(curr: Trie, i: int = 0):
            if i == len(word):
                return curr.is_end

            if len(curr.children)==0 or word[i] not in curr.children:
                return False

            return check(curr.children[word[i]],i + 1)


        return check(curr)

    def getAllWord(self):
        curr = self.root
        path = ""
        answer = []

        def get(curr,path):
            path += curr.char
            if curr.is_end == True:
                answer.append(path)
                print(path)

            for child in curr.children.values():
                get(child,path)

            path = path[:-1]

        get(curr,path)
        return answer

    def getSuggestion(self, word : str):

        curr = self.root
        word = word.casefold()
        path = ""
        suggestions = []
        minimumDistance = 10e9
        def levenshtein(self, word1: str, word2: str) -> int:
            l = np.full((len(word1) + 1, len(word2) + 1), 10e9)

            for i in range(len(word1) + 1):
                l[i][0] = i

            for i in range(len(word2) + 1):
                l[0][i] = i

            for i in range(1, len(word1) + 1):
                for j in range(1, len(word2) + 1):
                    x = l[i - 1][j - 1] if word1[i - 1] == word2[j - 1] else min(l[i - 1][j], l[i][j - 1],l[i - 1][j - 1]) + 1
                    l[i][j] = x

            return int(l[len(word1)][len(word2)])

        def get(curr):
            nonlocal minimumDistance, suggestions,path

            if len(path)-len(word) > minimumDistance or minimumDistance == 0:
                return

            path += curr.char

            if curr.is_end == True:
                distance = levenshtein(self,word,path)

                #if distance > minimumDistance:
                 #   path = path[:-1]
                 #   return

                if distance == minimumDistance:
                    suggestions.append(path)

                elif distance < minimumDistance:
                    minimumDistance = distance
                    suggestions = [path]

            for child in curr.children.values():
                get(child)

            path = path[:-1]

        get(curr)
        print(minimumDistance)
        return suggestions


    def getAllCharacter(self):

        curr = self.root
        answer = []

        def dfs(curr):
            answer.append(curr.char)
            for key, child in curr.children.items():
                dfs(child)
        dfs(curr)
        return answer[1:]

