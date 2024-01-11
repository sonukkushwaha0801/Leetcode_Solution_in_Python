# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from collections import Counter, defaultdict


def exist(self, board: list[list[str]], word: str) -> bool:
	boardDic = defaultdict(int)
	for i in range(len(board)):
		for j in range(len(board[0])):
			boardDic[board[i][j]] += 1

	wordDic = Counter(word)
	for c in wordDic:
		if c not in boardDic or boardDic[c] < wordDic[c]:
			return False

	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == word[0]:
				if self.dfs(i, j, 0, board, word):
					return True

	return False

def dfs(self, i, j, k, board, word):
	if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or k >= len(word) or word[k] != board[i][j]:
		return False

	if k == len(word) - 1:
		return True

	directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

	for x, y in directions:
		tmp = board[i][j]
		board[i][j] = -1

		if self.dfs(i + x, j + y, k + 1, board, word): 
			return True

		board[i][j] = tmp

# Another way:
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        vis = set()

        def dfs(r, c, cur):
            if cur == len(word):
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or word[cur] != board[r][c] or (r, c) in vis:
                return False
            
            vis.add((r, c))

            check = (dfs(r + 1, c, cur + 1) or
                    dfs(r - 1, c, cur + 1) or
                    dfs(r, c + 1, cur + 1) or
                    dfs(r, c - 1, cur + 1))
                    
            vis.remove((r, c))

            return check
        
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        return False