class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        res = set()
        index = 0

        def dfs(r, c, word, word_trie):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited:
                return False

            if board[r][c] not in word_trie.children:
                return 
            
            visited.add((r,c))
            word += board[r][c]
            word_trie = word_trie.children[board[r][c]]
            if word in words:
                res.add(word)
            
            if word_trie.children:
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    dfs(r + dr, c + dc, word, word_trie)
            visited.remove((r,c))


        res = []
        word_trie = Trie()
        for word in words:
            word_trie.add(word)
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, "", word_trie.root)
        return list(res)
            