# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(cur_node, parent):
            if cur_node == None:
                return 0
            moves = dfs(cur_node.left, cur_node) + dfs(cur_node.right, cur_node)
            from_this = cur_node.val - 1
            parent.val += from_this
            moves += abs(from_this)
            return moves
    
        return dfs(root, TreeNode())
    
# Another way:

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        
        def post_order(node):
            if not node:
                return 0
            
            left_balance = post_order(node.left)
            right_balance = post_order(node.right)
            
            # Total balance for the current node
            balance = node.val + left_balance + right_balance - 1
            
            # Add the number of moves required to balance the current node
            self.moves += abs(balance)
            
            # Return the balance to the parent node
            return balance
        
        post_order(root)
        return self.moves