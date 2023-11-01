# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def findMode(self, root) :
        def in_order_traversal(node):
            nonlocal current_val, current_count, max_count, modes
            if not node:
                return
            
            in_order_traversal(node.left)
            
            current_count = current_count + 1 if node.val == current_val else 1
            current_val = node.val
            
            if current_count > max_count:
                max_count = current_count
                modes = [current_val]
            elif current_count == max_count:
                modes.append(current_val)
            
            in_order_traversal(node.right)
            
        current_val = None
        current_count = 0
        max_count = 0
        modes = []
        in_order_traversal(root)
        return modes

# Another way:
class Solution:
    def findMode(self, root):
        
        if root is None:
            return []
        
        self.mode = []
        self.max_count = 0
        self.prev = None
        self.count = 0
        
        self.inorder(root)
        
        return self.mode
    
    def inorder(self, root):
            
            if root is None:
                return
            
            self.inorder(root.left)
            
            if self.prev is None:
                self.prev = root.val
                self.count = 1
            elif self.prev == root.val:
                self.count += 1
            else:
                self.prev = root.val
                self.count = 1
            
            if self.count > self.max_count:
                self.max_count = self.count
                self.mode = [root.val]
            elif self.count == self.max_count:
                self.mode.append(root.val)
            
            self.inorder(root.right)