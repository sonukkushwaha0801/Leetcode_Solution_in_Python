# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        f = s = head
        count  = 0
        for i in range(k):
            count +=1
            if not f.next:
                f = s
                break
            f = f.next 
        for i in range(k%count):
            f = f.next
        if f == s:
            return f
        while f.next:
            f = f.next
            s = s.next
        temp = s.next
        s.next = None
        f.next = head
        return temp
    
# Another way:

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head

        if head.next == None: return head
        new_head = head
        t = head
        c = 0
        while t:
            t = t.next
            c = c + 1

        n = int(k%c)

        while n != 0:
            new_head = self.rotate(new_head)
            n = n - 1

        return new_head

    def rotate(self,head):
        dummy = ListNode(-200,head)
        ls = head
        cur = head.next
        while cur:
            if cur.next == None:
                break
            cur = cur.next
            ls = ls.next

        ls.next = None
        cur.next = dummy.next
        dummy.next = cur
        return dummy.next