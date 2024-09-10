# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# type first :
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        head.next = ListNode(gcd(head.val, head.next.val), self.insertGreatestCommonDivisors(head.next))
        return head
    
# Another way:
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node.next:
            node.next = ListNode(gcd(node.val, node.next.val), node.next)
            node = node.next.next
        return head