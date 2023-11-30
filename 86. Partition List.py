# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before, after = ListNode(0), ListNode(0)
        before_curr, after_curr = before, after
        
        while head:
            if head.val < x:
                before_curr.next, before_curr = head, head
            else:
                after_curr.next, after_curr = head, head
            head = head.next
        
        after_curr.next = None
        before_curr.next = after.next
        
        return before.next
    
# Another way:

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        d1=c1=ListNode(0)
        d2=c2=ListNode(0)
        while head:
            if head.val<x:
                d1.next=head
                d1=d1.next

            else:
                d2.next=head
                d2=d2.next    

            head=head.next

        d2.next=None
        d1.next=c2.next
        return c1.next    