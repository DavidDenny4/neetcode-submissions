class TreeNode:
    def __init__(self): 
        self.word = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TreeNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        
        index = 0
        def dfs(node):
            if (index + 1) == len(word):
                return node.word

            if word[index] == ".":
                for c in node.children:
                    index += 1
                    if dfs(node.children[c], index + 1):
                        return True
                return False
            else:
                if word[index + 1] not in node.children:
                    return False
                index += 1
                return dfs(node.children[word[index + 1]])

        return dfs(self.root)