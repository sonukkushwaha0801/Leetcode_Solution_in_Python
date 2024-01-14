# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:

    def makeTree(self,mat):
        s = sum([sum(x) for x in mat])
        n = len(mat)
        if s==0 or s==n*n:
            return Node(s//(n*n),1,None,None,None,None)
        
        topm = mat[:n//2]
        botm = mat[n//2:]

        topml = list(map(lambda x:x[:n//2],topm))
        topmr = list(map(lambda x:x[n//2:],topm))
        botml = list(map(lambda x:x[:n//2],botm))
        botmr = list(map(lambda x:x[n//2:],botm))

        tl = self.makeTree(topml)
        tr = self.makeTree(topmr)
        bl = self.makeTree(botml)
        br = self.makeTree(botmr)

        return Node(1,0,tl,tr,bl,br)

    def construct(self, grid: List[List[int]]) -> 'Node':

        return self.makeTree(grid)

# Another way:
class Solution:
    def construct(self, grid: List[List[int]]) -> Node:
        
        def construct_helper(grid):
            if len(grid) == 1:
                return Node(val=bool(grid[0][0]), isLeaf=True)
            
            all_same = all(all(val == grid[0][0] for val in row) for row in grid)
            if all_same:
                return Node(val=bool(grid[0][0]), isLeaf=True)
            
            node = Node(isLeaf=False)
            
            n = len(grid)
            mid = n // 2
            top_left = [row[:mid] for row in grid[:mid]]
            top_right = [row[mid:] for row in grid[:mid]]
            bottom_left = [row[:mid] for row in grid[mid:]]
            bottom_right = [row[mid:] for row in grid[mid:]]
            
            node.topLeft = construct_helper(top_left)
            node.topRight = construct_helper(top_right)
            node.bottomLeft = construct_helper(bottom_left)
            node.bottomRight = construct_helper(bottom_right)
            
            return node
    
        return construct_helper(grid)