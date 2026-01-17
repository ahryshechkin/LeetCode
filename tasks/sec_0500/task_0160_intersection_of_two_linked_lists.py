from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hA, hB = headA, headB

        while hA != hB:
            hA = hA.next if hA else headB
            hB = hB.next if hB else headA

        return hA