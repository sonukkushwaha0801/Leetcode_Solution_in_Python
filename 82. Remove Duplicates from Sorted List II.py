# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next:
            if current.next.next and current.next.val == current.next.next.val:
                # We found a duplicate.
                # Iterate until we reach a distinct value.
                val = current.next.val
                while current.next and current.next.val == val:
                    current.next = current.next.next
            else:
                # Move to the next node.
                current = current.next

        return dummy.next 
    
# Another way:
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        temp=head
        dummy=pre=ListNode()
        while temp and temp.next:
            if temp.val==temp.next.val:
                while temp and temp.next and temp.val==temp.next.val:
                    temp=temp.next
                temp=temp.next
                pre.next=temp
            else:
                pre.next=temp
                pre=pre.next
                temp=temp.next
        return dummy.next