# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from collections import defaultdict


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        
        def dfs(x, y, root):
            letter = board[x][y]
            cur = root[letter]
            word = cur.pop('#', False)
            if word:
                res.append(word)
            board[x][y] = '*'
            for dirx, diry in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                curx, cury = x + dirx, y + diry
                if 0 <= curx < m and 0 <= cury < n and board[curx][cury] in cur:
                    dfs(curx, cury, cur)
            board[x][y] = letter
            if not cur:
                root.pop(letter)
                
        trie = {}
        for word in words:
            cur = trie
            for letter in word:
                cur = cur.setdefault(letter, {})
            cur['#'] = word
            
        m, n = len(board), len(board[0])
        res = []
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i, j, trie)
        
        return res

# ANother way:
class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        res = []
        Trie = lambda : defaultdict(Trie)
        root = Trie()
        def add(s):
            cur = root
            for c in s: cur = cur[c]
            cur['$'] = s
                
        for word in words: add(word)
        m, n = len(board), len(board[0])
        
        def dfs(i, j, root):
            ch = board[i][j]
            cur = root.get(ch)
            if not cur: return 

            if '$' in cur: 
                res.append(cur['$'])
                del cur['$']
            
            board[i][j] = '#'
            if i<m-1: dfs(i+1, j, cur)
            if i>0: dfs(i-1, j, cur)
            if j<n-1: dfs(i, j+1, cur)
            if j>0: dfs(i, j-1, cur)
            board[i][j] = ch

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
        return res
    
    