# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        temp = merged

        while l1 and l2 :
            if l1.val < l2.val :
                temp.next = l1
                l1 = l1.next
            else :
                temp.next = l2
                l2 = l2.next

            temp = temp.next

        if l1:
            temp.next = l1
        else :
            temp.next = l2

        return merged.next                   
    
# Another way:
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = dummyHead = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                dummyHead.next = list1
                list1 = list1.next
            else:
                dummyHead.next = list2
                list2 = list2.next
            dummyHead = dummyHead.next
        
        if list1:
            dummyHead.next = list1
        if list2:
            dummyHead.next = list2
        return newHead.next