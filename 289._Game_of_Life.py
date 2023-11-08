# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                
                # count number of live neighbours
                live_neighbours = 0
                for x in range(max(i-1, 0), min(i+2, m)):
                    for y in range(max(j-1, 0), min(j+2, n)):
                        if i == x and j == y:
                            continue
                        live_neighbours += board[x][y] % 2
                
                # mark the cell if it needs to change states
                if board[i][j] == 0:
                    if live_neighbours == 3:
                        board[i][j] = 2
                elif live_neighbours < 2 or live_neighbours > 3:
                    board[i][j] = 3
        
        # change all required states
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0

# Another way:
class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        life = []
        for i in range(len(board)):
            col = []
            for j in range(len(board[0])):
                col.append(board[i][j])
            life.append(col)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 1:
                    if self.check(board,i,j) == True:
                        life[i][j] = 0
                else:
                    if self.check(board,i,j) == True:
                        life[i][j] = 1
        for i in range(len(life)):
            for j in range(len(life[0])):
                board[i][j] = life[i][j]
                
    def check(self,board,i,j):
        count = 0
        if board[i][j]==1:
            #diagonal top left to bottom right
            if i !=0 and j !=0 :
                if board[i-1][j-1] == 1:
                    count+=1
            if i != len(board)-1 and j != len(board[0])-1:
                if board[i+1][j+1] == 1:
                    count+=1
            #diagonal top right to bottom left
            if i!=0 and j != len(board[0])-1:
                if board[i-1][j+1] ==1:
                    count+=1
            if i!= len(board)-1 and j!=0:
                if board[i+1][j-1] == 1:
                    count +=1
            #top and bottom vertically
            if i!=0 and board[i-1][j]==1:
                count+=1
            if i!= len(board)-1 and board[i+1][j]==1:
                count +=1
            #left and right horizontally
            if j!=0 and board[i][j-1] ==1:
                count+=1
            if j!= len(board[0])-1 and board[i][j+1]==1:
                count+=1
            if count ==2 or count == 3:
                return False
            else:
                return True
        else:
            if board[i][j]==0:
                #diagonal top left to bottom right
                if i !=0 and j !=0 :
                    if board[i-1][j-1] == 1:
                        count+=1
                if i != len(board)-1 and j != len(board[0])-1:
                    if board[i+1][j+1] == 1:
                        count+=1
                #diagonal top right to bottom left
                if i!=0 and j != len(board[0])-1:
                    if board[i-1][j+1] ==1:
                        count+=1
                if i!= len(board)-1 and j!= 0:
                    if board[i+1][j-1] ==1:
                        count +=1
                #top and bottom vertically
                if i!=0 and board[i-1][j]==1:
                    count+=1
                if i!= len(board)-1 and board[i+1][j]==1:
                    count +=1
                #left and right horizontally
                if j!=0 and board[i][j-1] ==1:
                    count+=1
                if j!= len(board[0])-1 and board[i][j+1]==1:
                    count+=1
                if count == 3:
                    return True
                else:
                    return False 