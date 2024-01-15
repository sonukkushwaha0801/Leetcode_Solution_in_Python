# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from typing import List, Optional
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = len(lists)
        if len(lists) == 0 or lists is None:
            return None
        
        def merge_2_linkedlist(l1, l2):
            dummy = ListNode()
            tail = dummy
            while l1 and l2:
                if l1.val > l2.val:
                    tail.next = l2
                    l2 = l2.next
                else:
                    tail.next = l1
                    l1 = l1.next
                tail = tail.next

            while l1:
                tail.next = l1
                l1 = l1.next
                tail = tail.next

            while l2:
                tail.next = l2
                l2 = l2.next
                tail = tail.next

            return dummy.next
                
        while len(lists) > 1:
            answer = []
            for i in range(0, len(lists), 2):
                left_arr = lists[i]
                if i+1 < len(lists):
                    right_arr = lists[i+1]
                else:
                    right_arr = None

                answer.append(merge_2_linkedlist(left_arr, right_arr))
            lists = answer
        return lists[0]


# Another way:
class Solution:
    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        dummy = ListNode(-1)
        temp = dummy
        while left and right:
            if left.val < right.val:
                temp.next = left
                temp = temp.next
                left = left.next
            else:
                temp.next = right
                temp = temp.next
                right = right.next
        while left:
            temp.next = left
            temp = temp.next
            left = left.next
        while right:
            temp.next = right
            temp = temp.next
            right = right.next
        return dummy.next
    
    def mergeSort(self, lists: List[ListNode], start: int, end: int) -> ListNode:
        if start == end:
            return lists[start]
        mid = start + (end - start) // 2
        left = self.mergeSort(lists, start, mid)
        right = self.mergeSort(lists, mid + 1, end)
        return self.merge(left, right)
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        return self.mergeSort(lists, 0, len(lists) - 1)