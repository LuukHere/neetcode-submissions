# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr, twoStep = head, head

        while twoStep and twoStep.next:
            curr = curr.next
            twoStep = twoStep.next.next
            if curr == twoStep:
                return True

        return False
