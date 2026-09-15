class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:

            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()

                curr = curr.children[char]

            curr.word = word

        
        rows = len(board)
        cols = len(board[0])
        result = []

        def dfs(r, c, node):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or 
                board[r][c] == "#"
            ):
                return

            char = board[r][c]

            if char not in node.children:
                return

            node = node.children[char]

            if node.word:
                result.append(node.word)
                node.word = None

            board[r][c] = "#"

            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)

            board[r][c] = char

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result
