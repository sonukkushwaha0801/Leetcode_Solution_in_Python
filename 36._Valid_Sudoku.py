# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
from collections import defaultdict


class Solution(object):
    def isValidSudoku(self, board):
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(res) == len(set(res))

# Another way:
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        if not board:
            return False
        for row in board:
            temp = [i for i in row if i != '.']
            if len(set(temp)) != len(temp):
                return False

        transpose_dict = defaultdict(list)
        for row in board:
            for i in range(len(row)):
                if row[i] != '.':
                    transpose_dict[i].append(row[i])
        for k, v in transpose_dict.items():
            if len(v) != len(set(v)):
                return False

        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                box = []
                for k in range(i, i + 3):
                    box.extend(board[k][j:j + 3])

                box = [element for element in box if element != '.']
                if len(box) != len(set(box)):
                    return False
        return True