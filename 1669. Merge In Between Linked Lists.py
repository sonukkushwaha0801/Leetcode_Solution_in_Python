# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        ptr = list1
        for _ in range(a - 1):
            ptr = ptr.next
        
        qtr = ptr.next
        for _ in range(b - a + 1):
            qtr = qtr.next
        
        ptr.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = qtr
        
        return list1

# Another way:
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp1=list2
        head=list1
        pos=list2
        end=list1
        while list2.next:
            list2=list2.next
        i,j=0,0
        while list1:
            if i==a-1:
                pos=list1
            if j==b:
                end=list1
            i+=1
            j+=1
            list1=list1.next
        pos.next=temp1
        list2.next=end.next
        return head