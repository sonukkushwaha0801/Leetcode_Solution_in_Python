# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        node_to_lvl = {}
        lvls = defaultdict(list)

        def dfs(node, height):
            if not node:
                return 0
            height += 1
            left = dfs(node.left, height) + 1
            right = dfs(node.right, height) + 1
            node_to_lvl[node.val] = height
            heapq.heappush(lvls[height], (-max(left, right) - height + 1, height, node.val))
            return max(left, right)
        
        dfs(root, -1)
        res = []

        for q in queries:
            lvl = node_to_lvl[q]
            if q == root.val:
                res.append(0)
            elif len(lvls[lvl]) == 1:
                res.append(lvls[lvl - 1][0][1])
            elif lvls[lvl][0][2] == q:
                temp = heapq.heappop(lvls[lvl])
                res.append(-lvls[lvl][0][0])
                heapq.heappush(lvls[lvl], temp)
            elif lvls[lvl][0][2] != q:
                res.append(-lvls[lvl][0][0])
        
        return res
            