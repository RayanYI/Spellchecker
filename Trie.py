from TrieNode import TrieNode


class Trie:

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        currentNode = self.root

        for i in range(len(word)):

            if word[i] not in currentNode.children:
                currentNode.children[word[i]] = TrieNode(word[i], i == len(word) - 1)
            elif i == len(word) - 1:
                currentNode.children[word[i]].is_end = True

            currentNode = currentNode.children[word[i]]

    def checkWord(self, word: str):
        curr = self.root

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

    def getAllCharacter(self):

        curr = self.root
        answer = []

        def dfs(curr):
            answer.append(curr.char)
            for key, child in curr.children.items():
                dfs(child)
        dfs(curr)
        return answer[1:]

