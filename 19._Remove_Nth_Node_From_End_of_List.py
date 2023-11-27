# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp:
            count +=1
            temp = temp.next
        if count == 1:
            return None    
        temp = head
        count = count - n +1
        if count == 1 :
            return head.next
        while (count -2 ):  
            temp = temp.next
            count -= 1  
        if n == 1:
            temp.next = None
        else:
            temp.next = temp.next.next       
        return head

# Another way:
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head
        for i in range(n):
            fast = fast.next    
        if not fast:
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head

        