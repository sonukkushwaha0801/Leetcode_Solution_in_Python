# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        top = None
        current = head            
        leftTail = None

        i = 1
        
        while i <= right: 
            if i < left:
                leftTail =  current                
                current = current.next
            else:                
                nextNode = current.next
                current.next = top
                top = current
                current = nextNode
            i +=1
        if leftTail and current:
            leftTail.next.next = current
            leftTail.next = top       
        elif not leftTail and current:
            head.next = current
            head = top
        elif not current and leftTail:
            leftTail.next = top
        else:
            head = top

        return head
        
# Another way:

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        cur = prev.next
        for _ in range(right - left):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next


        
        

        