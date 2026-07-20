# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
       result = ListNode(0)  # Dummy node to simplify the result construction
       ptr = result
       carry = 0

        # Traverse both lists
       while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            ptr.next = ListNode(total % 10)
            ptr = ptr.next

            # Move to next nodes
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

       return result.next
