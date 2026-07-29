class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        numSet = set(nums)

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        current = head

        while current:

            if current.val in numSet:
                prev.next = current.next

            else:
                prev = current

            current = current.next

        return dummy.next