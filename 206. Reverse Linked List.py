# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        current_node = head

        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        return prev_node
    
# another way:
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p0, p1= None, head
        while p1:
            p1.next, p2= p0, p1.next
            p0, p1 = p1, p2
        return p0  