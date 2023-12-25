# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        rows = len(board)
        columns = len(board[0])
        def mark_edge (row,col):
            if row < 0 or row > rows -1 or col < 0 or col > columns -1 or board[row][col] != "O":
                return
            board[row][col] = "B"
            mark_edge(row-1,col)
            mark_edge(row+1,col)
            mark_edge(row,col-1)
            mark_edge(row,col+1)

        
        for row in range(rows):
            for col in range(columns):
                if board[row][col] == "O":
                    if row == 0 or row == rows -1 or col == 0 or col == columns-1:
                        mark_edge(row,col)   
        for row in range(rows):
            for col in range(columns):
                if board[row][col] != "B":
                    board[row][col] = "X"
                if board[row][col] == "B":
                    board[row][col] = "O"

# Another way:
class Solution:
    def solve(self, board):
        nrows = len(board)
        ncols = len(board[0])
        not_surrounded = set()

        def dfs(row, col):
            if row not in range(nrows) or col not in range(ncols) or board[row][col] == "X" or (row, col) in not_surrounded:
                return

            not_surrounded.add((row, col))

            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)


        
        for row in range(nrows):
            for col in range(ncols):
                if (row == 0 or col == 0 or row == nrows-1 or col == ncols-1) and (row, col) not in not_surrounded and board[row][col] == "O":
                    dfs(row, col)

        for row in range(nrows):
            for col in range(ncols):
                if (row, col) not in not_surrounded:
                    board[row][col]="X"