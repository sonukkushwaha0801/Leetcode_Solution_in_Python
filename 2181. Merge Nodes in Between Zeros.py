# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        currentNew = dummy
        currentOld = head.next 

        sum = 0
        
        while currentOld is not None:
            if currentOld.val == 0:
                if sum != 0:
                    currentNew.next = ListNode(sum)
                    currentNew = currentNew.next
                    sum = 0 
            else:
                sum += currentOld.val
            currentOld = currentOld.next

        return dummy.next
    
# Another way:
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head.next
        prev = ListNode(0,head)
        while current != None:
            s = 0
            prev = prev.next
            while current.val != 0:
                s += current.val
                current = current.next
            
            prev.val = s
            current = current.next
        
        prev.next = None

        return head