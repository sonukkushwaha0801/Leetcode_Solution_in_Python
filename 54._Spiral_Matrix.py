# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix)
        n = len(matrix[0])
        answer = []
        direction = [[1,0],[0,-1],[-1,0],[0,1]]
        visited = []
        for i in range(m):
            visited.append([0]*n)
        def traverse(coord, index):
            if coord[0] >= m or coord[0] < 0 or coord[1] >= n or coord[0] < 0 or visited[coord[0]][coord[1]] == 1:
                return
            answer.append(matrix[coord[0]][coord[1]])
            visited[coord[0]][coord[1]] = 1
            coord2 = [a + b for a, b in zip(coord, direction[index])]
            if coord2[0] >= m or coord2[0] < 0 or coord2[1] >= n or coord2[0] < 0 or visited[coord2[0]][coord2[1]] == 1:
                index = (index + 1) % 4
            coord2 = [a + b for a, b in zip(coord, direction[index])]
            traverse(coord2, index)
        traverse([0,0],3)
        return answer 
    
# Another way:
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix:
            return []

        result = []
        top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        
        while top <= bottom and left <= right:
            # Traverse right
            for i in range(left, right+1):
                result.append(matrix[top][i])
            top += 1
            
            # Traverse down
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right -= 1
            
            # Traverse left
            if top <= bottom:
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            
            # Traverse up
            if left <= right:
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left += 1
                
        return result