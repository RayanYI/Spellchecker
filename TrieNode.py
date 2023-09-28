class TrieNode:

    def __init__(self, char: str, is_end: bool = False):
        self.char = char
        self.is_end = is_end
        self.children = {}