# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:


class Solution:
   def deleteNode(self, node):
       node.val, node.next=node.next.val, node.next.next
       