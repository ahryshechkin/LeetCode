from unittest import TestCase, main
from tasks.sec_0500.task_0021_merge_two_sorted_lists import Solution


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TestSolution(TestCase):
    s = Solution()


    def test01(self):
        h14 = ListNode(4)
        h12 = ListNode(2, h14)
        h11 = ListNode(1, h12)

        h24 = ListNode(4)
        h23 = ListNode(3, h24)
        h21 = ListNode(1, h23)

        r = list()
        head = self.s.mergeTwoLists(h11, h21)
        while head:
            r.append(head.val)
            head = head.next
        self.assertListEqual(r, [1, 1, 2, 3, 4, 4])


    def test02(self):
        r = list()
        head = self.s.mergeTwoLists([], [])
        while head:
            r.append(head.val)
            head = head.next
        self.assertListEqual(r, [])


    def test03(self):
        r = list()
        head = self.s.mergeTwoLists([], ListNode())
        while head:
            r.append(head.val)
            head = head.next
        self.assertListEqual(r, [0])