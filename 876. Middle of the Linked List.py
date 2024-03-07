# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start=head
        end=head
        while start and start.next:
            start,end=start.next.next,end.next
        return end
    
# Another way:
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow