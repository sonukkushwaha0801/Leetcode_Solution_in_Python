# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def sortList(self, head):
        def merge(a,b):
            cur = res = ListNode()
            
            while a and b:
                if a.val <= b.val:
                    cur.next = a 
                    a = a.next 
                else:
                    cur.next = b 
                    b = b.next 
                    
                cur = cur.next
                
            while a:
                cur.next = a 
                a = a.next 
                cur = cur.next
                
            while b:
                cur.next = b 
                b = b.next 
                cur = cur.next
                
            return res.next
            
        if not head or not head.next:
            return head 
        
        pre, slow, fast = None, head, head
        
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
            
        if pre:
            pre.next = None
            
        first_half = self.sortList(head)
        second_half = self.sortList(slow)
        result = merge(first_half, second_half)
        
        return result
    
# Another way:
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp
        
        left = self.sortList(left)
        right = self.sortList(right)
        
        return self.merge(left, right)
    
    def getMid(self, head):
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    # Merge the list
    def merge(self, list1, list2):
        newHead = tail = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                tail.next = list2
                list2 = list2.next
            else:
                tail.next = list1
                list1 = list1.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        
        return newHead.next
        