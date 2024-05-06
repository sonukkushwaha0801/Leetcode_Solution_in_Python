# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

class Solution:
    def removeNodes(self, n: Optional[ListNode]) -> Optional[ListNode]:
        return n.next and (setattr(n,'next',q:=self.removeNodes(n.next)),q)[n.val<q.val] or n
    
# Another way:
class Solution:
    def removeNodes(self, n: Optional[ListNode]) -> Optional[ListNode]:
        if n.next:
            q = self.removeNodes(n.next)
            n.next = q
            if n.val < q.val:
                return q

        return n