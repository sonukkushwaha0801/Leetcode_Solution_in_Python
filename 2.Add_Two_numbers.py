# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result

# Another way:
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tail = ListNode((l1.val + l2.val) % 10)
        head = tail
        remainder = (l1.val + l2.val) // 10
        l1, l2 = l1.next, l2.next
        
        while l1 is not None and l2 is not None:
            sum_column = l1.val + l2.val + remainder
            tail.next = ListNode(sum_column % 10)
            tail = tail.next
            remainder = sum_column // 10
            l1, l2 = l1.next, l2.next
        
        while l1 is not None:
            sum_column = l1.val + remainder
            tail.next = ListNode(sum_column % 10)
            tail = tail.next
            remainder = sum_column // 10
            l1 = l1.next
        
        while l2 is not None:
            sum_column = l2.val + remainder
            tail.next = ListNode(sum_column % 10)
            tail = tail.next
            remainder = sum_column // 10
            l2 = l2.next
        
        if remainder:
            tail.next = ListNode(remainder)
        
        return head